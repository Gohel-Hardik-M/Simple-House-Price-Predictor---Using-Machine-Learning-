import pickle 
from flask import Flask , render_template , redirect , request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/action',methods=['GET','POST'])
def action():
      if request.method == 'POST':
        condition = request.form['condition']
        location = request.form['location']
        area = request.form['area']
        garage = request.form['garage']
        year_build = request.form['yearBuilt']
        floors= request.form['floors']
        bathrooms = request.form['bathrooms']
        bedrooms = request.form['bedrooms']
        
        location_map = {'Downtown':1,'Suburban':2,'Rural':3,'Urban':4}
        Garage_map = {'Yes':1,'No':0}
        condition_map = {'Excellent':1,'Good':2,'Poor':3,'Fair':4}
        
        main_location = location_map[location]
        main_garage = Garage_map[garage]
        main_condition = condition_map[condition]
        
        with open('House Price Prediction/house_price_model.pkl','rb') as f:
            model = pickle.load(f)
        
        price = model.predict([[area,bedrooms,bathrooms,floors,year_build,main_location,main_condition,main_garage]])
        return render_template('index.html',predicted_p = price[0])
    


    

if __name__ == '__main__':
    app.run(debug=True)
    
    