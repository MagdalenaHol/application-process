from flask import Flask, render_template, request, url_for, redirect

import data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors')
def mentors_list():
    mentor_name = request.args.get('mentor-last-name')
    city_name = request.args.get('city-name')

    if mentor_name:
        mentor_info = data_manager.get_mentors_by_last_name(mentor_name)
    elif city_name:
        mentor_info = data_manager.get_city_name(city_name)
    else:
        mentor_info = data_manager.get_mentors()

    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    return render_template('mentors.html', mentors=mentor_info, cites=mentor_info)


@app.route('/applicant-phone')
def applicant_searching():
    applicant_first_name = request.args.get('applicant-first-name')
    applicant_last_name = request.args.get('applicant-last-name')

    if applicant_first_name or applicant_last_name:
        applicant_info = data_manager.get_applicant_data_by_name(applicant_first_name)

    return render_template('index.html', applicants=applicant_info)


if __name__ == '__main__':
    app.run(debug=True)
