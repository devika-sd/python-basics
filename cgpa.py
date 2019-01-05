def eee(sem):
    eee=[[["HS8151","Communicative English","4"],["MA8151","Engineering Mathematics - I","4"],["PH8151"," Engineering Physics","3"],["CY8151","Engineering Chemistry","3"],["GE8151"," Problem Solving and Python Programming","3"],["GE8152","Engineering Graphics ","4"],["GE8161"," Problem Solving and Python Programming Laboratory","2"],["BS8161"," Physics and Chemistry Laboratory","2"]],[["HS8251","Technical English","4"],["MA8251","Engineering Mathematics - II ","4"],["PH8253","physics for Electronics Engineering","3"],["BE8252","Basic Civil and Mechanical Engineering","4"],["EE8251","Circuit Theory","3"],["GE8291","Environmental Science and Engineering","3"],["GE8261","Engineering Practices Laboratory","2"],["EE8261","Electric Circuits Laboratory ","2"]],[["MA8353 ","Transforms and Partial Differential Equations ","4"],["EE8351","Digital Logic Circuits  ","3"],["EE8391","Electromagnetic Theory ","3"],["EE8301","Electrical Machines - I","3"],["EC8353","Electron Devices and Circuits","3"],["ME8792","Power Plant Engineering","3"],["EC8311","Electronics Laboratory","2"],["EE8311","Electrical Machines Laboratory - I","2"]],[["MA8491","Numerical Methods ","4"],["EE8401","Electrical Machines - II","3"],["EE8402 ","Transmission and Distribution ","3"],["EE8403 ","Measurements and Instrumentation ","3"],["EE8451","Linear Integrated Circuits and  Applications","3"],["IC8451 ","Control Systems ","4"],["EE8411 ","Electrical Machines Laboratory - II","2"],["EE8461 ","Linear and Digital Integrated Circuits Laboratory","2"],["EE8412 ","Technical Seminar ","1"]],[["EE8501 ","Power System Analysis ","3"],["EE8551 ","Microprocessors and Microcontrollers ","3"],["EE8552 ","Power Electronics ","3"],["EE8591 ","Digital Signal Processing ","3"],[ "CS8392 ","Object Oriented Programming ","3"],[" ","Open Elective I*  ","3"],["EE8511","Control and Instrumentation Laboratory ","2"],["HS8581","Professional Communication","1"],["CS8383","Object Oriented Programming Laboratory ","2"]],[["EE8601","Solid State Drives","3"],["EE8602 ","Protection and Switchgear","3"],["EE8691","Embedded Systems","3"],[" ","Professional Elective I","3"],[" ","Professional Elective II ","3"],["EE8661 ","Power Electronics and Drives Laboratory ","2"],["EE8681 ","Microprocessors and Microcontrollers Laboratory ","2"],["EE8611 ","Mini Project  ","2"]],[["EE8701 ","High Voltage Engineering ","3"],["EE8702 ","Power System Operation and Control ","3"],["EE8703","Renewable Energy Systems","3"],[" ","Open Elective II*","3"],[" ","Professional  Elective III","3"],[" ","Professional Elective IV ","3"],["EE8711 ","Power System Simulation Laboratory ","2"],["EE8712 ","Renewable Energy Systems Laboratory ","2"]],[[" ","Professional Elective V  ","3"],[" ","Professional Elective VI ","3"],["EE8811","Project Work ","10"]]]
    return eee[sem]

present=int(input("enter the sem"))
semester=eee(present+1)
print(eee(present))
print(semester[0][1])
#semester carries thier subject
for i in semester:
    print(i[0],i[1],i[2])
    

    


