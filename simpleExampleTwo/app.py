from flask import Flask, render_template
import pandas as pd
import matplotlib
# this is needed to run on the mac due to a threading issue
matplotlib.use('Agg')
# enables the currency display in matplotlib
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import base64
import io

app = Flask(__name__)

@app.route('/')
def plot():
    df = pd.read_csv('data.csv')  # Reading the CSV data
    fig, ax = plt.subplots()
 #   Define a function to format values as currency
    formatter = FuncFormatter(lambda x, pos: "${:,.0f}".format(x))

    # Apply the formatter to the y-axis
    ax.yaxis.set_major_formatter(formatter)
    df.plot(kind='bar', x='Year', y=['Male', 'Female'], ax=ax)  # Creating a bar plot

    # Calcuate the wage gap for the most recent Year
    last_row = df.iloc[-1]
    wage_gap = last_row['Male'] - last_row['Female']

    # annotate the wage gap on the plot
    ax.text(len(df) - 1, max(last_row['Male'], last_row['Female']), "${:,.0f}".format(wage_gap),
            verticalalignment='bottom', horizontalalignment='center')

    ax.set_title('Monthly Earnings Male versus Female in California')
    plt.tight_layout()

    # Converting plot to PNG image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('plot.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)