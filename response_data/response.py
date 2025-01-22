# response data
intent_responses = {
    "COLLEGE_OVERVIEW": "Baba Farid College of Engineering and Technology (BFCET) is committed to providing quality education and fostering research in various fields of engineering and technology. Our vision is to create a center of excellence in education and innovation.",
    
    "COURSE_QUERY": "We offer a variety of undergraduate and postgraduate programs such as B.Tech, M.Tech, Mechanical Engineering, Civil Engineering, CSE, Computer Science, AI & ML, and more. Please feel free to ask for more specific details about any course.",
    
    "ADMISSION_QUERY": "To apply for admission to BFCET, you need to fill out the online application form. The admission process typically involves entrance exams, followed by document verification. Please check our website for deadlines and further details.",
    
    "CAMPUS_QUERY": "Our campus has state-of-the-art facilities including a library, canteen, gym, student lounge, and outdoor spaces. We also have hostels for outstation students, and Wi-Fi is available throughout the campus.",
    
    "FACULTY_QUERY": "Our faculty consists of highly qualified and experienced professors, including department heads and teaching staff. The college is headed by our Principal, who ensures the overall academic and administrative activities run smoothly.",
    
    "DEPARTMENT_QUERY": "We have several departments including the Computer Science Department, Mechanical Engineering Department, Civil Engineering Department, Electrical Engineering Department, and more. Each department is well-equipped with the necessary infrastructure for both learning and research.",
    
    "FEE_QUERY": "The fee structure varies depending on the program and level of study. For detailed information, please check the 'Fees & Scholarships' section on our website. We also provide scholarship options and financial aid for eligible students.",
    
    "PLACEMENT_AND_CAREER_QUERY": "BFCET has a dedicated placement cell that helps students secure internships and job placements in reputed companies. The highest package offered so far is in the range of X Lakhs per annum, and we have an excellent placement track record.",
    
    "ALUMNI_NETWORK_QUERY": "BFCET has a strong alumni network that regularly interacts with current students through mentorship programs, career counseling, and guest lectures. Our alumni also contribute by helping students with internships and placement opportunities.",
    
    "EVENT_AND_ACTIVITES_QUERY": "BFCET organizes various extracurricular activities throughout the year, including annual festivals, cultural events, sports competitions, and academic workshops. Students are encouraged to participate in these events to enhance their overall experience.",
    
    "RESEARCH_OPPORTUNITIES_QUERY": "Our college provides several research opportunities, especially for postgraduate and PhD students. We have dedicated research centers in areas like AI, ML, Robotics, and Renewable Energy. Faculty members often collaborate with students on research projects.",
    
    "INTERNATIONAL_COLLABORATION_QUERY": "BFCET has partnerships with several international universities, enabling students to take part in exchange programs, study abroad opportunities, and collaborative research projects. We aim to provide global exposure to our students.",
    
    "ONLINE_LEARNING_AND_RESOURCES_QUERY": "BFCET offers a variety of online learning resources including virtual labs, recorded lectures, and access to online journals. Students can also participate in online certification programs and e-learning courses.",
    
    "FALLBACK": "Sorry, I didn't quite get that. Could you please rephrase or provide more details about your query?"
}

def get_responses(intent):
    """
    This function returns the intent-responses mapping.
    """
    return intent_responses.get(intent, "FALLBACK")

if __name__ == "__main__":
    print("Response module loaded successfully.")