from flask import Flask, render_template, request, jsonify
from vakioveikkaus import luo_rivit, laske_jakauma, muotoile_jakauma

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html', title="Vakioveikkausrivien Generaattori")
    except Exception as e:
        app.logger.error(f"Virhe index-sivun renderöinnissä: {str(e)}")
        return "Virhe sivun lataamisessa", 500

@app.route('/generoi', methods=['POST'])
def generoi():
    try:
        data = request.json
        maara = data['maara']
        painotukset = data['painotukset']
        
        rivit = luo_rivit(maara, painotukset)
        jakauma = laske_jakauma(rivit)
        muotoiltu_jakauma = muotoile_jakauma(jakauma, maara)
        
        return jsonify({
            'rivit': rivit,
            'jakauma': muotoiltu_jakauma
        })
    except Exception as e:
        app.logger.error(f"Virhe rivien generoinnissa: {str(e)}")
        return jsonify({'error': 'Virhe rivien generoinnissa'}), 500

if __name__ == '__main__':
    app.run(debug=True)