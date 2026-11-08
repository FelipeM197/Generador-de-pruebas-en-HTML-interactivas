"""Generador de interfaz web interactiva y autocontenida en HTML para evaluaciones."""
import base64
import html
import json
import mimetypes
import os
import re
import unicodedata


def _imagen_a_data_uri(ruta):
    if not ruta or not os.path.isfile(ruta):
        return None
    tipo_mime, _ = mimetypes.guess_type(ruta)
    tipo_mime = tipo_mime or "image/png"
    with open(ruta, 'rb') as archivo:
        datos_base64 = base64.b64encode(archivo.read()).decode('ascii')
    return f"data:{tipo_mime};base64,{datos_base64}"


def _generar_slug(texto):
    normalizado = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')
    slug = re.sub(r'[^a-zA-Z0-9]+', '_', normalizado).strip('_').lower()
    return slug or "examen"


_ETIQUETAS_TIPO = {
    "MULTIPLE": "opción múltiple",
    "CORTA": "respuesta corta",
    "RELACION": "relación",
    "VERDADERO_FALSO": "verdadero/falso",
}


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITULO__</title>
<style>
:root {
  --primary:#2563eb; --primary-dark:#1d4ed8; --bg:#f1f5f9; --card-bg:#ffffff;
  --text:#1e293b; --muted:#64748b; --success:#16a34a; --success-bg:#dcfce7;
  --error:#dc2626; --error-bg:#fee2e2; --border:#e2e8f0;
}
* { box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; background:var(--bg); color:var(--text); margin:0; padding:1rem; line-height:1.55; }
.container { max-width: 880px; margin:0 auto; padding-bottom:4rem; }
.header { background:var(--card-bg); padding:1.6rem 2rem; border-radius:14px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.08); margin-bottom:1.2rem; border-top:5px solid var(--primary); }
.header h1 { margin:0 0 .3rem; font-size:1.5rem; }
.header p.sub { margin:0; color:var(--muted); font-size:.92rem; }

.toolbar { display:flex; flex-wrap:wrap; gap:.6rem; margin-top:1rem; }
.btn { background:var(--primary); color:#fff; border:none; padding:9px 16px; border-radius:8px; font-size:.9rem; font-weight:600; cursor:pointer; transition:background .15s; }
.btn:hover { background:var(--primary-dark); }
.btn.secundario { background:#64748b; }
.btn.secundario:hover { background:#475569; }
.btn.peligro { background:#fff; color:var(--error); border:1.5px solid var(--error); }
.btn.peligro:hover { background:var(--error-bg); }
.btn:disabled { background:#cbd5e1; color:#94a3b8; cursor:not-allowed; }

.historial-box { margin-top:1rem; font-size:.85rem; color:var(--muted); background:#f8fafc; border:1px solid var(--border); border-radius:8px; padding:.8rem 1rem; }
.historial-box strong { color:var(--text); }
.historial-item { display:inline-block; margin:2px 10px 2px 0; }

.progreso-wrap { background:var(--card-bg); border-radius:10px; padding:.8rem 1.2rem; margin-bottom:1.2rem; box-shadow:0 2px 4px rgba(0,0,0,.05); display:flex; align-items:center; gap:1rem; font-size:.9rem; }
.progreso-bar-bg { flex:1; background:#e2e8f0; border-radius:6px; height:10px; overflow:hidden; }
.progreso-bar { background:var(--primary); height:100%; width:0%; transition:width .3s; }

.pregunta-card { background:var(--card-bg); border-radius:14px; box-shadow:0 4px 6px -1px rgba(0,0,0,0.08); padding:1.8rem; margin-bottom:1.3rem; }
.pregunta-badge { display:inline-block; background:#e0e7ff; color:var(--primary); padding:4px 12px; border-radius:20px; font-size:.78rem; font-weight:700; margin-bottom:12px; letter-spacing:.02em; }
.pregunta-badge.fallada { background:#fee2e2; color:var(--error); }
.enunciado { font-weight:600; font-size:1.08rem; margin-bottom:1.3rem; white-space:pre-wrap; color:#0f172a; }

.pregunta-imagen { margin:0 0 1.3rem; text-align:center; }
.pregunta-imagen img { max-width:100%; max-height:420px; border-radius:8px; border:1px solid var(--border); background:#fff; }

.opcion-label { display:flex; align-items:flex-start; background:#f8fafc; padding:12px 14px; margin-bottom:8px; border-radius:8px; border:2px solid transparent; cursor:pointer; transition:all .15s; font-size:.96rem; }
.opcion-label:hover { background:#f1f5f9; border-color:#cbd5e1; }
.opcion-label input { margin-right:10px; margin-top:3px; transform:scale(1.2); cursor:pointer; flex-shrink:0; }
.opcion-label.correcta { background:var(--success-bg); border-color:#86efac; }
.opcion-label.incorrecta { background:var(--error-bg); border-color:#fca5a5; }

.vf-opciones { display:flex; gap:14px; margin:4px 0 6px; }
@media (max-width: 480px) { .vf-opciones { flex-direction:column; } }
.vf-boton { flex:1; display:flex; align-items:center; justify-content:center; gap:10px; padding:16px; border-radius:10px; border:2px solid #cbd5e1; background:#f8fafc; cursor:pointer; font-weight:700; font-size:1.02rem; transition:all .15s; }
.vf-boton:hover { background:#f1f5f9; border-color:#94a3b8; }
.vf-boton input { transform:scale(1.25); cursor:pointer; }
.vf-boton.correcta { background:var(--success-bg); border-color:#86efac; color:#166534; }
.vf-boton.incorrecta { background:var(--error-bg); border-color:#fca5a5; color:#991b1b; }

.input-text { width:100%; padding:13px; border:2px solid #cbd5e1; border-radius:8px; font-size:1rem; margin-top:6px; background:#f8fafc; }
.input-text:focus { border-color:var(--primary); outline:none; background:#fff; }

.relacion-ayuda { font-size:.85rem; color:var(--muted); margin-bottom:.9rem; }
.relacion-columnas { display:grid; grid-template-columns:1fr; gap:1.4rem; margin-bottom:1rem; }
@media (min-width: 680px) { .relacion-columnas { grid-template-columns:1.15fr 1fr; } }
.columna-a-lista { display:flex; flex-direction:column; gap:8px; }
.columna-b-lista { background:#f1f5f9; border:1px solid var(--border); border-radius:10px; padding:1rem 1.1rem; display:flex; flex-direction:column; gap:9px; }
.columna-b-titulo { font-size:.8rem; font-weight:700; color:var(--muted); text-transform:uppercase; letter-spacing:.03em; margin-bottom:2px; }
.item-b { font-size:.9rem; color:#334155; background:#fff; padding:8px 11px; border-radius:6px; border:1px solid var(--border); }
.item-b strong { color:var(--primary); }

.relacion-fila { display:flex; align-items:center; gap:10px; background:#f8fafc; padding:10px 12px; border-radius:8px; border:2px solid transparent; }
.relacion-fila.correcta { background:var(--success-bg); border-color:#86efac; }
.relacion-fila.incorrecta { background:var(--error-bg); border-color:#fca5a5; }
.relacion-num { flex-shrink:0; width:26px; height:26px; border-radius:50%; background:var(--primary); color:#fff; font-weight:700; font-size:.85rem; display:flex; align-items:center; justify-content:center; }
.relacion-texto { flex:1; font-size:.93rem; }
.relacion-input { flex-shrink:0; width:44px; text-align:center; text-transform:uppercase; font-weight:700; font-size:1rem; padding:8px 4px; border:2px solid #94a3b8; border-radius:6px; color:var(--primary); background:#fff; }
.relacion-input:focus { border-color:var(--primary); outline:none; }
.relacion-input:disabled { background:#f1f5f9; }

.btn-validar { margin-top:14px; }
.feedback { margin-top:1.1rem; padding:1rem 1.1rem; border-radius:8px; display:none; white-space:pre-wrap; font-size:.92rem; }
.feedback.correcto { background:var(--success-bg); color:#166534; display:block; border:1px solid #86efac; }
.feedback.incorrecto { background:var(--error-bg); color:#991b1b; display:block; border:1px solid #fca5a5; }

#resultado-final { background:var(--card-bg); padding:2.6rem 2rem; border-radius:14px; text-align:center; margin-top:2rem; display:none; border:3px solid var(--primary); }
#resultado-final .btn { margin:6px; }
#sin-preguntas { display:none; text-align:center; padding:3rem; color:var(--muted); }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <h1>__TITULO__</h1>
    <p class="sub">__SUBTITULO__</p>
    <div class="toolbar">
      <button class="btn" onclick="reiniciarExamen(false)">Reiniciar examen</button>
      <button class="btn secundario" id="btn-falladas" onclick="reiniciarExamen(true)">Repasar solo falladas (<span id="conteo-falladas">0</span>)</button>
      <button class="btn peligro" onclick="borrarHistorial()">Borrar historial</button>
    </div>
    <div class="historial-box" id="historial-resumen"></div>
  </div>

  <div class="progreso-wrap" id="progreso-wrap">
    <span id="progreso-texto">0 / 0</span>
    <div class="progreso-bar-bg"><div class="progreso-bar" id="progreso-bar"></div></div>
  </div>

  <form id="formulario-examen" onsubmit="return false;"></form>
  <div id="sin-preguntas">No hay preguntas falladas registradas todavia. Responde el examen completo primero.</div>
  <div id="resultado-final"></div>
</div>

<script>
const ID_EXAMEN = "__ID_EXAMEN__";
const BASE_DATOS = __DATOS_JSON__;
const CLAVE_HISTORIAL = `examen_${ID_EXAMEN}_historial`;
const CLAVE_FALLAS = `examen_${ID_EXAMEN}_fallas`;

let preguntasActivas = [];

function normalizar(texto) {
  if (!texto) return "";
  return texto.toString().normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .toLowerCase().replace(/[^a-z0-9]/g, '');
}

function barajar(elementos) {
  const copia = elementos.slice();
  for (let i = copia.length - 1; i > 0; i--) {
    const aleatorio = Math.floor(Math.random() * (i + 1));
    [copia[i], copia[aleatorio]] = [copia[aleatorio], copia[i]];
  }
  return copia;
}

function leerFallas() {
  try { return JSON.parse(localStorage.getItem(CLAVE_FALLAS) || '{}'); } catch (e) { return {}; }
}
function guardarFallas(obj) {
  try { localStorage.setItem(CLAVE_FALLAS, JSON.stringify(obj)); } catch (e) {}
}
function leerHistorial() {
  try { return JSON.parse(localStorage.getItem(CLAVE_HISTORIAL) || '[]'); } catch (e) { return []; }
}

function actualizarUI_Memoria() {
  const fallas = leerFallas();
  const idsFallados = Object.keys(fallas).filter(k => fallas[k] > 0);
  document.getElementById('conteo-falladas').textContent = idsFallados.length;
  document.getElementById('btn-falladas').disabled = idsFallados.length === 0;

  const hist = leerHistorial();
  const contenedorHistorial = document.getElementById('historial-resumen');
  if (hist.length === 0) {
    contenedorHistorial.innerHTML = "No hay intentos registrados para este examen.";
  } else {
    let contenido = "<strong>Últimos intentos:</strong> ";
    hist.slice(0, 6).forEach(h => {
      const color = h.porcentaje >= 70 ? 'var(--success)' : 'var(--error)';
      contenido += `<span class="historial-item">${h.fecha} &rarr; <strong style="color:${color}">${h.porcentaje}%</strong> (${h.correctas}/${h.total})</span>`;
    });
    contenedorHistorial.innerHTML = contenido;
  }
}

function reiniciarExamen(soloFalladas) {
  if (soloFalladas) {
    const fallas = leerFallas();
    const ids = new Set(Object.keys(fallas).filter(k => fallas[k] > 0));
    preguntasActivas = BASE_DATOS.filter(q => ids.has(q.id));
    if (preguntasActivas.length === 0) {
      document.getElementById('formulario-examen').innerHTML = "";
      document.getElementById('progreso-wrap').style.display = 'none';
      document.getElementById('resultado-final').style.display = 'none';
      document.getElementById('sin-preguntas').style.display = 'block';
      return;
    }
  } else {
    preguntasActivas = BASE_DATOS.slice();
  }
  document.getElementById('sin-preguntas').style.display = 'none';
  document.getElementById('progreso-wrap').style.display = 'flex';
  document.getElementById('resultado-final').style.display = 'none';
  preguntasActivas = barajar(preguntasActivas);
  preguntasActivas.forEach(q => { q.respondida = false; q.acertada = false; });
  renderizarExamen();
  actualizarProgreso();
  window.scrollTo({top: 0, behavior:'smooth'});
}

function borrarHistorial() {
  if (!confirm("Deseas borrar el historial de intentos y preguntas falladas de este examen?")) return;
  localStorage.removeItem(CLAVE_HISTORIAL);
  localStorage.removeItem(CLAVE_FALLAS);
  actualizarUI_Memoria();
}

function renderizarExamen() {
  const formulario = document.getElementById('formulario-examen');
  let contenido = "";
  preguntasActivas.forEach((q, idx) => {
    contenido += renderPregunta(q, idx);
  });
  formulario.innerHTML = contenido;
}

function etiquetaTipo(q) {
  if (q.tipo === 'MULTIPLE') return 'Opción múltiple';
  if (q.tipo === 'CORTA') return 'Respuesta corta';
  if (q.tipo === 'RELACION') return q.modo === 'numero' ? 'Ordenamiento' : 'Relación / Emparejamiento';
  if (q.tipo === 'VERDADERO_FALSO') return 'Verdadero o Falso';
  return q.tipo;
}

function renderPregunta(q, idx) {
  const fallas = leerFallas();
  const esFallada = (fallas[q.id] || 0) > 0;
  let bloque = `<div class="pregunta-card" id="card-${idx}">`;
  bloque += `<span class="pregunta-badge${esFallada ? ' fallada' : ''}">Pregunta ${idx + 1} de ${preguntasActivas.length} · ${etiquetaTipo(q)}${esFallada ? ' (fallada previamente)' : ''}</span>`;
  bloque += `<div class="enunciado">${escapeHtml(q.enunciado)}</div>`;
  if (q.imagen) {
    bloque += `<div class="pregunta-imagen"><img src="${q.imagen}" alt="Imagen de apoyo para pregunta ${idx + 1}" loading="lazy"></div>`;
  }

  if (q.tipo === 'MULTIPLE') {
    const opciones = barajar(q.opciones);
    opciones.forEach((opt, i) => {
      bloque += `<label class="opcion-label" id="op-${idx}-${i}">
        <input type="radio" name="q-${idx}" value="${i}" onchange="responderMultiple(${idx})">
        <span>${escapeHtml(opt)}</span>
      </label>`;
    });
    bloque += `<div id="opciones-data-${idx}" style="display:none">${escapeHtml(JSON.stringify(opciones))}</div>`;
  } else if (q.tipo === 'VERDADERO_FALSO') {
    const opciones = barajar(q.opciones);
    bloque += `<div class="vf-opciones">`;
    opciones.forEach((opt, i) => {
      const soloTexto = opt.replace(/^[A-Za-z][.)\-]\s*/, '');
      bloque += `<label class="vf-boton" id="op-${idx}-${i}">
        <input type="radio" name="q-${idx}" value="${i}" onchange="responderMultiple(${idx})">
        <span>${escapeHtml(soloTexto)}</span>
      </label>`;
    });
    bloque += `</div>`;
    bloque += `<div id="opciones-data-${idx}" style="display:none">${escapeHtml(JSON.stringify(opciones))}</div>`;
  } else if (q.tipo === 'CORTA') {
    bloque += `<input type="text" class="input-text" id="resp-${idx}" placeholder="Escribe tu respuesta" autocomplete="off" onkeydown="if(event.key==='Enter'){event.preventDefault();responderCorta(${idx});}">`;
    bloque += `<button class="btn btn-validar" onclick="responderCorta(${idx})">Validar respuesta</button>`;
  } else if (q.tipo === 'RELACION') {
    const esOrden = q.modo === 'numero';
    const colB = esOrden ? q.columna_b.slice() : barajar(q.columna_b);
    const ayuda = esOrden
      ? 'Escribe en cada casilla de la Columna A el número de posición que le corresponda (Columna B).'
      : 'Escribe en cada casilla de la Columna A la letra de la Columna B que le corresponda.';
    bloque += `<p class="relacion-ayuda">${ayuda}</p>`;
    bloque += `<div class="relacion-columnas">`;
    bloque += `<div class="columna-a-lista">`;
    q.columna_a.forEach((item) => {
      bloque += `<div class="relacion-fila" id="fila-${idx}-${item.num}">
        <div class="relacion-num">${item.num}</div>
        <div class="relacion-texto">${escapeHtml(item.texto)}</div>
        <input type="text" class="relacion-input" id="sel-${idx}-${item.num}" maxlength="2" autocomplete="off" placeholder="-">
      </div>`;
    });
    bloque += `</div>`;
    bloque += `<div class="columna-b-lista"><div class="columna-b-titulo">Columna B</div>`;
    colB.forEach(opt => {
      bloque += esOrden
        ? `<div class="item-b">${escapeHtml(opt.texto)}</div>`
        : `<div class="item-b"><strong>${escapeHtml(opt.letra.toUpperCase())}.</strong> ${escapeHtml(opt.texto)}</div>`;
    });
    bloque += `</div></div>`;
    bloque += `<button class="btn btn-validar" onclick="responderRelacion(${idx})">Validar respuestas</button>`;
  }

  bloque += `<div id="feed-${idx}" class="feedback"></div>`;
  bloque += `</div>`;
  return bloque;
}

function escapeHtml(cadena) {
  const contenedor = document.createElement('div');
  contenedor.textContent = cadena == null ? "" : String(cadena);
  return contenedor.innerHTML;
}

function marcarResultado(idx, acertada) {
  const q = preguntasActivas[idx];
  q.respondida = true;
  q.acertada = acertada;

  const fallas = leerFallas();
  fallas[q.id] = acertada ? 0 : 1;
  guardarFallas(fallas);
  actualizarUI_Memoria();

  const feedDiv = document.getElementById(`feed-${idx}`);
  feedDiv.className = 'feedback ' + (acertada ? 'correcto' : 'incorrecto');
  const titulo = acertada ? 'Correcto' : 'Incorrecto';
  const explicacionTexto = q.explicacion || q.feedback || '';
  feedDiv.innerHTML = `<strong>${titulo}</strong>${explicacionTexto ? '<p style="margin-top:8px;">' + escapeHtml(explicacionTexto) + '</p>' : ''}`;

  actualizarProgreso();
  verificarFinExamen();
}

function responderMultiple(idx) {
  const q = preguntasActivas[idx];
  if (q.respondida) return;
  const marcado = document.querySelector(`input[name="q-${idx}"]:checked`);
  if (!marcado) return;
  const opciones = JSON.parse(document.getElementById(`opciones-data-${idx}`).textContent);
  const elegido = opciones[parseInt(marcado.value, 10)];
  const letraElegida = (elegido.match(/^([A-Za-z])[.)\-]/) || [,''])[1].toUpperCase();
  const acertada = letraElegida === (q.respuesta_correcta || '').trim().toUpperCase();

  document.querySelectorAll(`input[name="q-${idx}"]`).forEach((r, i) => {
    r.disabled = true;
    const label = document.getElementById(`op-${idx}-${i}`);
    const letra = (opciones[i].match(/^([A-Za-z])[.)\-]/) || [,''])[1].toUpperCase();
    if (letra === (q.respuesta_correcta || '').trim().toUpperCase()) label.classList.add('correcta');
    else if (r.checked) label.classList.add('incorrecta');
  });

  marcarResultado(idx, acertada);
}

function responderCorta(idx) {
  const q = preguntasActivas[idx];
  if (q.respondida) return;
  const campoTexto = document.getElementById(`resp-${idx}`);
  if (!campoTexto.value.trim()) { alert('Escribe una respuesta antes de validar.'); return; }
  const respuestasValidas = String(q.respuesta_correcta || '').split(/[\/|]/).map(normalizar).filter(Boolean);
  const acertada = respuestasValidas.includes(normalizar(campoTexto.value));
  campoTexto.disabled = true;
  document.querySelector(`#card-${idx} .btn-validar`).style.display = 'none';
  if (!acertada) {
    const feedDiv = document.getElementById(`feed-${idx}`);
    marcarResultado(idx, false);
    const explicacionTexto = q.explicacion || q.feedback || '';
    feedDiv.innerHTML = `<strong>Incorrecto.</strong> La respuesta esperada era: <strong>${escapeHtml(q.respuesta_correcta)}</strong>${explicacionTexto ? '<p style="margin-top:8px;">' + escapeHtml(explicacionTexto) + '</p>' : ''}`;
    return;
  }
  marcarResultado(idx, true);
}

function normalizarValor(valor, esOrden) {
  if (!valor) return "";
  if (esOrden) {
    const match = valor.trim().match(/\d+/);
    return match ? String(parseInt(match[0], 10)) : "";
  }
  const match = valor.trim().toLowerCase().match(/[a-z]/);
  return match ? match[0] : "";
}

function responderRelacion(idx) {
  const q = preguntasActivas[idx];
  if (q.respondida) return;
  const esOrden = q.modo === 'numero';
  let completo = true;
  const seleccion = {};
  q.columna_a.forEach(item => {
    const inp = document.getElementById(`sel-${idx}-${item.num}`);
    const valor = normalizarValor(inp.value, esOrden);
    if (!valor) completo = false;
    seleccion[item.num] = valor;
  });
  if (!completo) {
    alert(esOrden ? 'Escribe un número de posición en cada casilla antes de validar.' : 'Escribe una letra en cada casilla antes de validar.');
    return;
  }

  let todasCorrectas = true;
  q.columna_a.forEach(item => {
    const correcta = q.respuesta_correcta[item.num];
    const fila = document.getElementById(`fila-${idx}-${item.num}`);
    const inp = document.getElementById(`sel-${idx}-${item.num}`);
    inp.disabled = true;
    inp.value = esOrden ? seleccion[item.num] : seleccion[item.num].toUpperCase();
    if (seleccion[item.num] === correcta) {
      fila.classList.add('correcta');
    } else {
      fila.classList.add('incorrecta');
      todasCorrectas = false;
    }
  });

  document.querySelector(`#card-${idx} .btn-validar`).style.display = 'none';
  if (!todasCorrectas) {
    const mapa = {};
    q.columna_b.forEach(o => mapa[o.letra] = o.texto);
    let detalle = (esOrden ? 'Orden correcto:\n' : 'Emparejamiento correcto:\n');
    q.columna_a.forEach(item => {
      const correcta = q.respuesta_correcta[item.num];
      detalle += esOrden
        ? `${item.num}. ${item.texto}  →  posición ${correcta}\n`
        : `${item.num}. ${item.texto}  →  ${correcta.toUpperCase()}) ${mapa[correcta] || ''}\n`;
    });
    const feedDiv = document.getElementById(`feed-${idx}`);
    marcarResultado(idx, false);
    feedDiv.innerHTML = `<strong>Hay errores en el ${esOrden ? 'orden' : 'emparejamiento'}.</strong><p style="margin-top:8px; white-space:pre-wrap;">${escapeHtml(detalle)}</p>`;
    return;
  }
  marcarResultado(idx, true);
}

function actualizarProgreso() {
  const total = preguntasActivas.length;
  const respondidas = preguntasActivas.filter(q => q.respondida).length;
  document.getElementById('progreso-texto').textContent = `${respondidas} / ${total} respondidas`;
  document.getElementById('progreso-bar').style.width = total ? `${(respondidas / total) * 100}%` : '0%';
}

function verificarFinExamen() {
  const todas = preguntasActivas.every(q => q.respondida);
  if (!todas) return;
  const correctas = preguntasActivas.filter(q => q.acertada).length;
  const total = preguntasActivas.length;
  const porcentaje = Math.round((correctas / total) * 100);

  const hist = leerHistorial();
  const fecha = new Date().toLocaleDateString() + ' ' + new Date().toLocaleTimeString([], {hour:'2-digit', minute:'2-digit'});
  hist.unshift({ fecha, correctas, total, porcentaje });
  try { localStorage.setItem(CLAVE_HISTORIAL, JSON.stringify(hist.slice(0, 10))); } catch (e) {}
  actualizarUI_Memoria();

  const div = document.getElementById('resultado-final');
  div.innerHTML = `
    <h2 style="margin:0; color:#334155;">Calificación Final</h2>
    <h1 style="font-size:3.6rem; color:${porcentaje >= 70 ? 'var(--success)' : 'var(--error)'}; margin:14px 0;">${correctas} / ${total}</h1>
    <p style="font-size:1.15rem; color:#475569;"><strong>${porcentaje}% de aciertos</strong></p>
    <button class="btn" onclick="reiniciarExamen(false)">Repetir examen completo</button>
    <button class="btn secundario" onclick="reiniciarExamen(true)">Repasar solo falladas</button>
  `;
  div.style.display = 'block';
  div.scrollIntoView({behavior:'smooth', block:'center'});
}

window.onload = function () {
  if (!BASE_DATOS || BASE_DATOS.length === 0) {
    document.getElementById('formulario-examen').innerHTML = "<h3 style='color:red;text-align:center;'>Error: no se cargaron preguntas.</h3>";
    return;
  }
  actualizarUI_Memoria();
  reiniciarExamen(false);
};
</script>
</body>
</html>
"""


def generar_html(preguntas, ruta_html, titulo="Examen de Práctica", subtitulo=None, id_examen=None, exam_id=None):
    if not preguntas:
        raise ValueError("No hay preguntas para generar el HTML.")

    for pregunta in preguntas:
        ruta_imagen = pregunta.get("imagen")
        if ruta_imagen:
            pregunta["imagen"] = _imagen_a_data_uri(ruta_imagen)

    identificador = id_examen or exam_id or _generar_slug(titulo)
    if subtitulo is None:
        conteo = {}
        for pregunta in preguntas:
            tipo = pregunta["tipo"]
            conteo[tipo] = conteo.get(tipo, 0) + 1
        partes = ", ".join(f"{v} {_ETIQUETAS_TIPO.get(k, k.lower())}" for k, v in conteo.items())
        subtitulo = f"{len(preguntas)} preguntas ({partes}). Progreso guardado localmente en el navegador."

    # Escapamos secuencias de cierre de etiquetas script para evitar inyeccion involuntaria
    datos_json = json.dumps(preguntas, ensure_ascii=False).replace("</", "<\\/")

    salida = HTML_TEMPLATE
    salida = salida.replace("__TITULO__", html.escape(titulo))
    salida = salida.replace("__SUBTITULO__", html.escape(subtitulo))
    salida = salida.replace("__ID_EXAMEN__", identificador)
    salida = salida.replace("__EXAM_ID__", identificador)
    salida = salida.replace("__DATOS_JSON__", datos_json)

    with open(ruta_html, 'w', encoding='utf-8') as archivo:
        archivo.write(salida)

    return identificador
