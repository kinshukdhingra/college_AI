# training data for semantic Similarity to Fine Tune the Model.

from sentence_transformers import InputExample

train_examples = [
    # 1. College Overview
    InputExample(texts=["What is the Vision of the College?", "Tell me about the College."], label=1.0),
    InputExample(texts=["Describe the college in brief.", "Give an overview of this institution."], label=1.0),
    InputExample(texts=["When was the college established?", "What is the history of this institution?"], label=1.0),
    InputExample(texts=["What is the motto of the college?", "Does the college have a mission statement?"], label=1.0),

    # 2. Courses Offered
    InputExample(texts=["What programs I can join after 12th?", "What courses are offered?"], label=1.0),
    InputExample(texts=["Do you offer undergraduate courses?", "What types of degrees can I pursue here?"], label=1.0),
    InputExample(texts=["Are there any diploma programs?", "Can I pursue certificate courses here?"], label=1.0),
    InputExample(texts=["Are part-time courses available?", "Do you offer evening or weekend classes?"], label=1.0),

    # 3. Admissions
    InputExample(texts=["How can I apply?", "What is the admission process?"], label=1.0),
    InputExample(texts=["Is there an entrance exam?", "What are the eligibility criteria for admission?"], label=1.0),
    InputExample(texts=["What documents are required for admission?", "Can I apply online for admission?"], label=1.0),
    InputExample(texts=["When does the admission process start?", "What are the key deadlines for applying?"], label=1.0),

    # 4. Campus Facility
    InputExample(texts=["Does this college have a library on campus?", "What are the facilities available here?"], label=1.0),
    InputExample(texts=["Do you provide hostel facilities?", "What infrastructure does the campus have?"], label=1.0),
    InputExample(texts=["Is there a cafeteria on campus?", "Are there any sports facilities available?"], label=1.0),
    InputExample(texts=["Does the college have Wi-Fi facilities?", "Are classrooms equipped with smart boards?"], label=1.0),

    # 5. Faculty
    InputExample(texts=["Who is the principal of the college?", "Who is Head of Department Of SSD?"], label=1.0),
    InputExample(texts=["Are the professors qualified?", "Who are some notable faculty members?"], label=1.0),
    InputExample(texts=["Do faculty members have industry experience?", "Are professors approachable for students?"], label=1.0),
    InputExample(texts=["How often do faculty members hold office hours?", "Is mentoring provided by faculty?"], label=1.0),

    # 6. Departments
    InputExample(texts=["How many Departments do you have?", "Does this college have the Engineering Department?"], label=1.0),
    InputExample(texts=["Is there a Computer Science department?", "What academic divisions are offered?"], label=1.0),
    InputExample(texts=["Do you have a Department of Humanities?", "Does the college offer medical-related departments?"], label=1.0),
    InputExample(texts=["Are there specialized departments for emerging fields?", "Is there a business school or management department?"], label=1.0),

    # 7. Fees Structure
    InputExample(texts=["What is the fee Structure?", "How much does a program cost?"], label=1.0),
    InputExample(texts=["Are there any scholarships available?", "Can you tell me about tuition fees?"], label=1.0),
    InputExample(texts=["Is there a difference in fees for international students?", "Are there installment options for fee payment?"], label=1.0),
    InputExample(texts=["Do you offer financial aid?", "What are the additional costs like hostel or library fees?"], label=1.0),

    # 8. Placement and Career Opportunities
    InputExample(texts=["What are the placement opportunities?", "Do students get campus placements?"], label=1.0),
    InputExample(texts=["What is the highest package offered?", "Do you have a career placement cell?"], label=1.0),
    InputExample(texts=["What companies visit for recruitment?", "What is the average placement percentage?"], label=1.0),
    InputExample(texts=["Are internships provided?", "Do you help students find internships?"], label=1.0),

    # 9. Alumni Network
    InputExample(texts=["Does the college have a strong alumni network?", "Who are some notable alumni?"], label=1.0),
    InputExample(texts=["Can alumni help students with placements?", "Is there an alumni association?"], label=1.0),
    InputExample(texts=["Do alumni frequently visit the campus?", "Are alumni involved in mentorship programs?"], label=1.0),
    InputExample(texts=["Does the college have an alumni portal?", "How does the alumni network support the institution?"], label=1.0),

    # 10. Events and Activities
    InputExample(texts=["What kind of extracurricular activities are available?", "Do you organize annual events?"], label=1.0),
    InputExample(texts=["Is there a cultural festival?", "Are sports facilities available for students?"], label=1.0),
    InputExample(texts=["Do you have student clubs or societies?", "Are there opportunities for community service?"], label=1.0),
    InputExample(texts=["Does the college celebrate national holidays?", "Are there leadership development programs?"], label=1.0),

    # 11. Research Opportunities
    InputExample(texts=["Does the college support research?", "Are there any research labs available?"], label=1.0),
    InputExample(texts=["Can I participate in research projects?", "Is there funding available for research?"], label=1.0),
    InputExample(texts=["Are research internships offered?", "Do faculty members collaborate with students on research?"], label=1.0),
    InputExample(texts=["Does the college publish a research journal?", "Is there a research center for PhD students?"], label=1.0),

    # 12. International Collaboration
    InputExample(texts=["Does the college have international partnerships?", "Can I participate in student exchange programs?"], label=1.0),
    InputExample(texts=["Are there opportunities to study abroad?", "Does the college offer global exposure?"], label=1.0),
    InputExample(texts=["Are foreign language courses available?", "Does the college have collaboration with global universities?"], label=1.0),
    InputExample(texts=["Are international internships facilitated?", "What are the options for cross-cultural learning?"], label=1.0),

    # 13. Online Learning and Resources
    InputExample(texts=["Are online courses available?", "Can students access digital libraries?"], label=1.0),
    InputExample(texts=["What e-learning tools are provided?", "Does the college use online learning platforms?"], label=1.0),
    InputExample(texts=["Is there access to virtual labs?", "Are recorded lectures provided?"], label=1.0),
    InputExample(texts=["Are students taught using online simulations?", "Do you offer online certification programs?"], label=1.0)
]
