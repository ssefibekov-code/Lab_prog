#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
import ast

from lab7_package import (
    linearize_recursive,
    get_sequence_a,
    make_calc,
    spiral_from_center
)

app = FastAPI(title="Лабораторная работа №7")


class LinearizeRequest(BaseModel):
    data: str


class SequenceRequest(BaseModel):
    n: int


class CalcRequest(BaseModel):
    operation: str
    initial: float
    values: List[float]


class SpiralRequest(BaseModel):
    size: int


# Простой HTML без сложного JavaScript
HTML_SIMPLE = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Лабораторная работа №7</title>
    <style>
        body { font-family: Arial; margin: 20px; background: #f0f0f0; }
        .container { max-width: 900px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; }
        h1 { text-align: center; color: #667eea; }
        .tab { display: inline-block; padding: 10px 20px; cursor: pointer; background: #ddd; margin-right: 5px; border-radius: 5px; }
        .tab.active { background: #667eea; color: white; }
        .content { display: none; margin-top: 20px; padding: 20px; background: #f9f9f9; border-radius: 10px; }
        .content.active { display: block; }
        input, select { padding: 8px; margin: 5px 0; width: 100%; max-width: 300px; }
        button { padding: 10px 20px; background: #667eea; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background: #5a67d8; }
        .result { margin-top: 20px; padding: 10px; background: #eef; border-radius: 5px; font-family: monospace; }
        hr { margin: 20px 0; }
    </style>
</head>
<body>
<div class="container">
    <h1>📚 Лабораторная работа №7</h1>
    <p style="text-align:center">Пакеты и модули | FastAPI (Well-done)</p>
    
    <div>
        <div class="tab active" onclick="showTab('tab1')">🔄 Рекурсия (ЛР4)</div>
        <div class="tab" onclick="showTab('tab2')">🔢 Замыкания (ЛР5)</div>
        <div class="tab" onclick="showTab('tab3')">🌀 Генераторы (ЛР6)</div>
    </div>
    
    <!-- Вкладка 1 -->
    <div id="tab1" class="content active">
        <h2>Линеаризация списков</h2>
        <input type="text" id="linearize-data" value="[1,2,[3,4,[5,6]]]" style="width:100%">
        <button onclick="linearize()">Линеаризовать</button>
        <div id="linearize-result" class="result"></div>
        
        <hr>
        
        <h2>Рекуррентная последовательность a_k</h2>
        <input type="number" id="seq-n" value="10">
        <button onclick="getSequence()">Вычислить</button>
        <div id="seq-result" class="result"></div>
    </div>
    
    <!-- Вкладка 2 -->
    <div id="tab2" class="content">
        <h2>Калькулятор с накоплением</h2>
        <select id="calc-op">
            <option value="+">+ (сложение)</option>
            <option value="-">- (вычитание)</option>
            <option value="*">* (умножение)</option>
            <option value="/">/ (деление)</option>
        </select><br>
        <input type="number" id="calc-initial" value="0" placeholder="Начальное значение"><br>
        <input type="text" id="calc-values" value="5,3,2,4" placeholder="Значения через запятую"><br>
        <button onclick="calculate()">Вычислить</button>
        <div id="calc-result" class="result"></div>
    </div>
    
    <!-- Вкладка 3 -->
    <div id="tab3" class="content">
        <h2>Спиральный обход матрицы от центра</h2>
        <select id="spiral-size">
            <option value="3">3x3</option>
            <option value="5" selected>5x5</option>
            <option value="7">7x7</option>
            <option value="9">9x9</option>
        </select><br>
        <button onclick="spiral()">Обойти</button>
        <div id="spiral-result" class="result"></div>
    </div>
</div>

<script>
    function showTab(tabId) {
        document.querySelectorAll('.content').forEach(el => el.classList.remove('active'));
        document.querySelectorAll('.tab').forEach(el => el.classList.remove('active'));
        document.getElementById(tabId).classList.add('active');
        event.target.classList.add('active');
    }
    
    async function linearize() {
        const data = document.getElementById('linearize-data').value;
        const resultDiv = document.getElementById('linearize-result');
        resultDiv.innerHTML = 'Загрузка...';
        try {
            const response = await fetch('/api/linearize', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({data: data})
            });
            const result = await response.json();
            if (result.success) {
                resultDiv.innerHTML = '<strong>Результат:</strong><br><pre>' + JSON.stringify(result.result, null, 2) + '</pre>';
            } else {
                resultDiv.innerHTML = '<strong>Ошибка:</strong> ' + result.error;
            }
        } catch(e) {
            resultDiv.innerHTML = '<strong>Ошибка:</strong> ' + e.message;
        }
    }
    
    async function getSequence() {
        const n = document.getElementById('seq-n').value;
        const resultDiv = document.getElementById('seq-result');
        resultDiv.innerHTML = 'Загрузка...';
        try {
            const response = await fetch('/api/sequence', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({n: parseInt(n)})
            });
            const data = await response.json();
            if (data.success) {
                let html = '<strong>Результат:</strong><br><pre>';
                for (let i = 0; i < data.values.length; i++) {
                    html += 'a_' + (i+1) + ' = ' + data.values[i] + '\\n';
                }
                html += '</pre>';
                resultDiv.innerHTML = html;
            } else {
                resultDiv.innerHTML = '<strong>Ошибка:</strong> ' + data.error;
            }
        } catch(e) {
            resultDiv.innerHTML = '<strong>Ошибка:</strong> ' + e.message;
        }
    }
    
    async function calculate() {
        const operation = document.getElementById('calc-op').value;
        const initial = parseFloat(document.getElementById('calc-initial').value);
        const valuesStr = document.getElementById('calc-values').value;
        const values = valuesStr.split(',').map(v => parseFloat(v.trim()));
        const resultDiv = document.getElementById('calc-result');
        resultDiv.innerHTML = 'Загрузка...';
        try {
            const response = await fetch('/api/calc', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({operation: operation, initial: initial, values: values})
            });
            const data = await response.json();
            if (data.success) {
                let html = '<strong>Результат:</strong><br><pre>';
                for (let i = 0; i < data.results.length; i++) {
                    html += data.results[i].input + ' -> ' + data.results[i].result + '\\n';
                }
                html += '</pre>';
                resultDiv.innerHTML = html;
            } else {
                resultDiv.innerHTML = '<strong>Ошибка:</strong> ' + data.error;
            }
        } catch(e) {
            resultDiv.innerHTML = '<strong>Ошибка:</strong> ' + e.message;
        }
    }
    
    async function spiral() {
        const size = parseInt(document.getElementById('spiral-size').value);
        const resultDiv = document.getElementById('spiral-result');
        resultDiv.innerHTML = 'Загрузка...';
        try {
            const response = await fetch('/api/spiral', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({size: size})
            });
            const data = await response.json();
            if (data.success) {
                let html = '<strong>Исходная матрица:</strong><br><pre>';
                for (let i = 0; i < data.matrix.length; i++) {
                    html += JSON.stringify(data.matrix[i]) + '\\n';
                }
                html += '</pre><strong>Порядок обхода:</strong><br><pre>';
                for (let i = 0; i < data.spiral_order.length; i++) {
                    const item = data.spiral_order[i];
                    html += '(' + item[0] + ', ' + item[1] + ') -> ' + item[2] + '\\n';
                }
                html += '</pre>';
                resultDiv.innerHTML = html;
            } else {
                resultDiv.innerHTML = '<strong>Ошибка:</strong> ' + data.error;
            }
        } catch(e) {
            resultDiv.innerHTML = '<strong>Ошибка:</strong> ' + e.message;
        }
    }
</script>
</body>
</html>
'''


@app.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse(content=HTML_SIMPLE)


@app.post("/api/linearize")
async def api_linearize(request: LinearizeRequest):
    try:
        data = ast.literal_eval(request.data)
        result = linearize_recursive(data)
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}


@app.post("/api/sequence")
async def api_sequence(request: SequenceRequest):
    try:
        values = get_sequence_a(request.n)
        return {"success": True, "values": values}
    except Exception as e:
        return {"success": False, "error": str(e)}


@app.post("/api/calc")
async def api_calc(request: CalcRequest):
    try:
        calc = make_calc(request.operation, request.initial)
        results = []
        current = request.initial
        for v in request.values:
            current = calc(v)
            results.append({"input": v, "result": current})
        return {"success": True, "results": results}
    except Exception as e:
        return {"success": False, "error": str(e)}


@app.post("/api/spiral")
async def api_spiral(request: SpiralRequest):
    try:
        size = request.size
        if size % 2 == 0:
            return {"success": False, "error": "Размер матрицы должен быть нечётным"}
        matrix = [[i * size + j + 1 for j in range(size)] for i in range(size)]
        spiral_order = list(spiral_from_center(matrix))
        return {"success": True, "matrix": matrix, "spiral_order": [(r, c, v) for r, c, v in spiral_order]}
    except Exception as e:
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)