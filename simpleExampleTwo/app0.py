from flask import Flask, render_template
import pandas as pd
import matplotlib
# this is needed to run on the mac due to a threading issue
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
import io

app = Flask(__name__)

@app.route('/')
def plot():
    df = pd.read_csv('sample.csv')  # Reading the CSV data
    fig, ax = plt.subplots()
    df.plot(kind='bar', x='Year', y=['Male', 'Female'], ax=ax)  # Creating a bar plot
    ax.set_title('Lifetime Earnings')
    plt.tight_layout()

    # Converting plot to PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('plot.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)