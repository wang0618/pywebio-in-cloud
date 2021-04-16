from pywebio.input import *
from pywebio.output import *


def main():
    """BMI Calculation

    Simple application for calculating Body Mass Index.
    """

    put_markdown("""# Body Mass Index
    
    [Body mass index](https://en.wikipedia.org/wiki/Body_mass_index) (BMI) is a measure of body fat based on height and weight that applies to adult men and women. 
    
    BMI Categories:
    
    | Category             | BMI           |
    | -------------------- | ------------- |
    | Severely underweight | BMI<14.9      |
    | Underweight          | 14.9≤BMI<18.4 |
    | Normal               | 18.4≤BMI<22.9 |
    | Overweight           | 22.9≤BMI<27.5 |
    | Moderately obese     | 27.5≤BMI<40   |
    | Severely obese       | BMI≥40        |
    
    ## BMI calculation
    """, strip_indent=4)

    info = input_group('BMI calculation', [
        input("Your Height(cm)", name="height", type=FLOAT),
        input("Your Weight(kg)", name="weight", type=FLOAT),
    ])

    BMI = info['weight'] / (info['height'] / 100) ** 2

    top_status = [(14.9, 'Severely underweight'), (18.4, 'Underweight'),
                  (22.9, 'Normal'), (27.5, 'Overweight'),
                  (40.0, 'Moderately obese'), (float('inf'), 'Severely obese')]

    for top, status in top_status:
        if BMI <= top:
            put_markdown('Your BMI: `%.1f`, Category: `%s`' % (BMI, status))
            break


if __name__ == '__main__':
    import argparse
    from pywebio.platform.tornado_http import start_server

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(main, port=args.port)
