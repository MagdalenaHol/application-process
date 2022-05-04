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
        mentor_details = data_manager.get_mentors_by_last_name(mentor_name)
    elif city_name:
        mentor_details = data_manager.get_city_name(city_name)
    else:
        mentor_details = data_manager.get_mentors()

    # We get back a list of dictionaries from the data_manager (for details check 'data_manager.py')

    return render_template('mentors.html', mentors=mentor_details, cites=mentor_details)


@app.route('/applicant-phone')
def applicant_searching():
    applicant_first_name = request.args.get('applicant-first-name')

    if applicant_first_name:
        applicant_details = data_manager.get_applicant_data_by_name(applicant_first_name)
    return render_template('index.html', applicants=applicant_details)


@app.route('/applicants-phone')
def applicant_search():
    email_ending = request.args.get('email-ending')
    if email_ending:
        applicant_details = data_manager.get_applicant_data_by_email_ending(email_ending)
    return render_template('index.html', applicants=applicant_details)


@app.route('/applicants', methods=['GET'])
def applicants_list():
    if request.method == "GET":
        applicant_details = data_manager.get_applicants()
        return render_template('applicants.html', applicants=applicant_details)


if __name__ == '__main__':
    app.run(debug=True)

