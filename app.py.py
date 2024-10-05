from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Carica i dati dall'Excel una volta all'avvio del server
catasto_df = pd.read_excel('catasto_chronicles_full.xlsx')

# Crea un endpoint per ottenere i dati del marker specifico
@app.route('/get_marker_data', methods=['GET'])
def get_marker_data():
    marker_id = request.args.get('id')  # Ottieni l'id del marker dalla richiesta

    # Filtra il DataFrame per trovare il record corrispondente a id_C
    marker_data = catasto_df[catasto_df['id_C'] == int(marker_id)]

    if marker_data.empty:
        return jsonify({'error': 'Marker not found'}), 404

    # Converte il record in un dizionario e restituisce il risultato come JSON
    marker_info = marker_data.to_dict(orient='records')[0]
    return jsonify(marker_info)

if __name__ == '__main__':
    app.run(debug=True)