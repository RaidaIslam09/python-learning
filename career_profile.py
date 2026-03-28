# ====================================================
# project 1 -Career Profile Script
# Author: Raida Tasnim Islam
# Description : A professional profile script using python variables, data types, and f-strings
# =====================================================

# --- Personal Information ---
__name__ ="Raida Tasnim Islam"
age = 28
height = 5.6
current_city = "Brooklyn"
current_state = "New York City"

# --- Education Profile ---
# --- bachelor degree ---
bachelor_degree ="Bachelor of Social Science"
bachelor_major ="Journalism and Mass Communication"
bachelor_university = "Daffodil Internation University "
bachelor_year = 2020
bachelor_country = "Bangladesh"

# --- masters 1 ---
masters_degree_1 = "Masters in Science"
masters_major_1 = "Management Information Systems"
masters_university_1 = "Lamar University"
masters_year_1 =2023
state_1 = "Texas"
city_1 = "Beaumont"
country ="United States of America"

# --- masters 2 ---
masters_degree_2 = "Masters in Science"
masters_major_2 = "Data Analytics"
masters_university_2 = "University of Cumberlands"
masters_year_2 = 2025
state_2 = "Kentucky"
city_2 = "Williamsburg"
country = "United States of America"

# phd (current) ---
current_degree = "Philosophy of Doctor"
current_major = "Information Technology"
current_university_3 = "University of Cumberlands"
phd_expected = 2030
state_3 = "Kentucky"
city_3 = "Williamsburg"
country = "United States of America"
is_phd_studnet = True

# --- Academic Projects ---
project1_name = "Guidelines on Electronic Mail Security"
project1_date = "March 2023-May 2023"
project1_university = "Lamar University"
project1_description = "Conducted extensive research on electronic mail security practices and identified common vulnerabilities and risks associated with email communication"

project2_name = "Understanding the NIST Cybersecurity Framework Core"
project2_date = "March 2023-May 2023"
project2_university = "Lamar University"
project2_description = "Analyzed the five core functions of the NIST Cybersecurity Framework — Identity, Protect, Detect, Respond, Recover — and their role in developing a robust cybersecurity posture"

project3_name = "Project Management in ERP"
project3_date = "September 2022-December 2022"
project3_university = "Lamar University"
project3_description = "Conducted thorough analysis of existing workflows and identified areas for improvement in efficiency and data management"    


# --- Career Goals ---
target_job = "Data Analyst"
target_city = "Dallas"
target_salary = 85000
years_to_goal = 4 

# ---Certification ---
cert1_name = "Google Data Analytics Professional Certificate"
cert1_issuer = "Coursera"
cert1_issued = "December 2023"
cert1_skills = "Data Visulization, Data Analysis, SQL Inquiry"

cert2_name = "Google Project Management Professional Certificate"
cert2_issuer = "Coursera"
cert2_issued = "October 2023"
cert2_skills = "Budgeting, Procurement, Data visulization, Project Management"


# =======================================
# Print Section
# ======================================

# --- print personal profile ---
print("=" * 50)
print("Professional Profile")
print("=" *50)
print(f"Name : {__name__}")
print(f"Age : {age}")
print(f"Heightv: {height}")
print(f"Location : {current_city}, {current_state}")
print(f"Status : PhD Student - {is_phd_studnet}")

# --- Education ---
print()
print("=" * 50)
print("Education Profile")
print("=" * 50)

print()
print(f"Bachelor's")
print(f"Degree = {bachelor_degree} in {bachelor_major}")
print(f"University = {bachelor_university}")
print(f"Location = {bachelor_country}")
print(f"year = {bachelor_year}")

print()
print(f"Masters 1")
print(f"Degree = {masters_degree_1} in {masters_major_1}")
print(f"University = {masters_university_1}")
print(f"Location = {state_1} in {city_1} in {country}")
print(f"year = {masters_year_1}")

print()
print(f"Masters 2")
print(f"Degree = {masters_degree_2} in {masters_major_2}")
print(f"University = {masters_university_2}")
print(f"Location = {state_2} in {city_2} in {country}")
print(f"year = {masters_year_2}")

print()
print(f"PhD - In Progress")
print(f"Degree = {current_degree} in {current_major}")
print(f"University = {current_university_3}")
print(f"Location = {state_3} in {city_3} in {country}")
print(f"year = {phd_expected}")

# --- Academic Projects ---
print()
print("=" * 50)
print("           ACADEMIC PROJECTS")
print("=" * 50)

print()
print(f"PROJECT 1")
print(f"Title: {project1_name}")
print(f"Date: {project1_date}")
print(f"University : {project1_university}")
print(f"Summary : {project1_description}")

print()
print(f"PROJECT 2")
print(f"Title: {project2_name}")
print(f"Date : {project2_date}")
print(f"University: {project2_university}")
print(f"Summary : {project2_description}")

print()
print(f"PROJECT 3")
print(f"Title : {project3_name}")
print(f"Date : {project3_date}")
print(f"University : {project3_university}")
print(f"Summary    : {project3_description}")

# --- Career Goals ---
print()
print("=" *50)
print("Data Types Check")
print("=" *50)
print(f"targer role : {target_job}")
print(f"target city  {target_city}")
print(f"target salary : ${target_salary}")
print(f"timeline : {years_to_goal} years")
print()

# --- Certifications ---
print()
print("=" * 50 )
print("Certifications")
print("=" * 50)

print(f"name : {cert1_name}")
print(f"issuer : {cert1_issuer}")
print(f"issued : {cert1_issued}")
print(f"skilss : {cert1_skills}")

print(f"name : {cert2_name}")
print(f"issuer : {cert2_issuer}")
print(f"issued : {cert2_issued}")
print(f"skilss : {cert2_skills}")


#--- Data Types ---
print()
print("=" * 50)
print("Data Types Check")
print("=" * 50)
print(f"name : {type(__name__)}")
print(f"bachelor_year : {type(bachelor_year)}")
print(f"masters_year : {type(masters_year_1)}")
print(f"masters_year : {type(masters_year_2)}")
print(f"target_salary : {type(target_salary)}")
print(f"is_phd_student: {type(is_phd_studnet)}")
print(f"years_to_goal : {type(years_to_goal)}")
print(f"cert1_name :{type(cert1_name)}")
print(f"cert1_name :{type(cert2_name)}")
print(f"project1_name : {type(project1_name)}")
print(f"project2_name : {type(project2_name)}")
print(f"project3_name : {type(project3_name)}")
print()
print("=" * 50)



