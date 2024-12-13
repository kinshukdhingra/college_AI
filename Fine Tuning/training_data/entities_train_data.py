TRAIN_DATA = [
    #College Overview
    ("Tell me about the BFCET", {"entities": [(18, 23, "COLLEGE")]}),
    ("Tell me about the Baba Farid College of Engineering and Technology", {"entities":[(18, 66, "COLLEGE")]}),
    ("Give an overview of BABA FARID COLLEGE.", {"entities": [(20, 38, "COLLEGE")]}),
    #Courses
    ("Does Baba Faird offers MBA or B.tech", {"entities":[(5, 15, "COLLEGE"), (23, 26, "COURSE"), (30, 36, "COURSE")]}),
    
    #Departments

    #Admission
    ("Tell me about the admission process in 2024", {"entities": [(14, 32, "PROCESS"), (37, 41, "YEAR")]}),

    #FreeStructure
    ("What is the fee structure for MBA?", {"entities": [(12, 26, "PROCESS"), (31, 34, "COURSE")]}),
    ("Can you explain the hostel fee?", {"entities": [(18, 28, "PROCESS")]}),

    #Faculty
]


# entities
'''
1. COLLEGE
2. COURSE
3. PROCESS
4. YEAR
'''