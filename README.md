# Rocket Sim
Simulatore di traiettoria di un razzo in Python.
Primo modello: lancio verticale con gravità, integrato con il metodo di Eulero e confrontato con la soluzione analitica.
Il drag riduce la quota massima da X m a Y m. Aumentare la massa avvicina la traiettoria al caso senza aria.
# Rocket Sim

Simulatore di traiettoria di un razzo in Python, costruito passo dopo passo
durante il primo anno di Ingegneria Aerospaziale.

## Obiettivo
Capire come si simula un moto fisico con l'integrazione numerica e come i
vari effetti (gravità, resistenza dell'aria, spinta) cambiano la traiettoria.

## Modelli implementati

### 1. Lancio verticale con gravità (`razzo.py`)
- Integrazione numerica con il metodo di Eulero (passo `dt`).
- Confronto con la soluzione analitica y = v0·t - ½·g·t².
- Osservazione: con `dt` grande l'errore cresce, perché Eulero assume la
  velocità costante durante ogni passo.

### 2. Lancio verticale con resistenza dell'aria (`razzo_drag.py`)
- Forza di drag: F = ½·ρ·Cd·A·v², sempre opposta al moto.
- Parametri: m = 1 kg, ρ = 1.225 kg/m³, Cd = 0.75, A = 0.005 m², v0 = 100 m/s.

| | Senza aria | Con aria |
|---|---|---|
| Quota massima | [0.00008+2.037736e3] m | [0.00084+2.037736e3] m |
| Tempo di volo | [20.380] s | [11.51] s |

## Cosa ho osservato
- Aumentando la massa, la traiettoria si avvicina a quella senza aria
  (l'accelerazione frenante è drag/m).
- Aumentando la sezione A, la traiettoria si allontana: il drag è
  proporzionale ad A.
- Aumentando la velocità iniziale, l'effetto dell'aria cresce più che
  proporzionalmente perché il drag dipende da v².
- Il parametro che conta è il coefficiente balistico m/(Cd·A).

## Come eseguirlo
pip3 install numpy matplotlib
python3 razzo.py
python3 razzo_drag.py

## Prossimi passi
- [ ] Spinta del motore e perdita di massa
- [ ] Densità dell'aria variabile con la quota
- [ ] Traiettoria 2D con angolo di lancio