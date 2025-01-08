#!/usr/bin/env python3
"""
    Team Allocator Module
"""


def student_list():
    return ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'BusiJHB2022 - 2 May - Durban Virtual',
    'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1', 'CebiJHB2022 - 2 May - Durban Virtual',
    'lukhona - 4 April - Phokeng Virtual', 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
    'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
    'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
    'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
    'zimthandilehDBN2022 - 4 April - Johannesburg Virtual','kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
    'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual','hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
    'zizonkehDBN2022 - 4 April - Johannesburg Virtual','sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
    'kholekileDBN2022 - 4 April - Johannesburg Virtual','vusiDBN2022 - 4 April - Durban Physical - seat 9',
    'kholelwahDBN2022 - 4 April - Johannesburg Virtual','zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
    'thembelahDBN2022 - 4 April - Johannesburg Virtual','babazileDBN2022 - 4 April - Durban Physical - seat 11',
    'thembisileDBN2022 - 4 April - Johannesburg Virtual','owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
    'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town physical',
    'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
    'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
    'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - Cape Town Virtual']


def dbn_campus_students(student_list):
    """
    Filters for attendees at the Durban campus from the full student list.
    """
    dbn_students = []
    for student in student_list:
        if "Durban" in student:
            dbn_students.append(student)

    return (dbn_students)


def dbn_physical_students(dbn_students):
    """
    Filters for physical attendees at the Durban campus.
    """
    dbn_physical_students_list = []
    for student in dbn_students:
        if "Physical" in student:
            dbn_physical_students_list.append(student)

    return (dbn_physical_students_list)


def dbn_physical_teams(dbn_physical_students_list):
    """
    Divides the physical Durban attendees into teams of 4.
    """
    dbn_physical_teams_list = []
    team = []

    for student in dbn_physical_students_list:
        team.append(student)
        if len(team) == 4:
            dbn_physical_teams_list.append(team)
            team = []  # reset

    if team:
        dbn_physical_teams_list.append(team)

    return (dbn_physical_teams_list)


def dbn_teams_file(dbn_physical_teams_list):
    """
    Writes the physical Durban teams into a text file.
    """
    with open("dbn_teams.txt", "w") as file:
        for team_number, team in enumerate(dbn_physical_teams_list, start=1):
            file.write(f"Team {team_number}:\n")
            for student in team:
                file.write(f"  {student}\n")
            file.write("\n")  # blank line between teams


def cpt_campus_students(student_list):
    """
    Filters for attendees at the Cape Town campus from the full sttudent list.
    """
    cpt_students = []
    for student in student_list:
        if "Cape Town" in student:
            cpt_students.append(student)

    return (cpt_students)


def cpt_physical_students(cpt_students):
    """
    Filters for the physical attendees at the Cape Town campus.
    """
    cpt_physical_students_list = []
    for student in cpt_students:
        if "Physical" in student:
           cpt_physical_students_list.append(student) 
    
    return (cpt_physical_students_list)


def cpt_physical_teams(cpt_physical_students_list):
    """
    Divides the physical Cape Town atendees into teams of 4.
    """
    cpt_physical_teams_list =[]
    team = []

    for student in cpt_physical_students_list:
        team.append(student)
        if len(team) == 4:
            cpt_physical_teams_list.append(team)
            team = []

    if team:
        cpt_physical_teams_list.append(team)

    return (cpt_physical_teams_list)


def cpt_teams_file(cpt_physical_teams_list):
    """
    Writes the physical Cape Town teams into a text file.
    """
    with open("cpt_teams.txt", "w") as file:
        for team_number, team in enumerate(cpt_physical_teams_list, start=1):
            file.write(f"Team {team_number}:\n")
            for student in team:
                file.write(f"  {student}\n")
            file.write("\n")


def jhb_campus_students(student_list):
    """
    Filters for attendees at the Johannesburg campus from the full student list.
    """
    jhb_students = []
    for student in student_list:
        if "Johannesburg" in student:
            jhb_students.append(student)

    return (jhb_students)


def jhb_physical_students(jhb_students):
    """
    Filters for physical attendees at the Johannesburg campus 
    """
    jhb_physical_students_list = []
    for student in jhb_students:
        if "Physical" in student:
            jhb_physical_students_list.append(student)

    return (jhb_physical_students_list)


def jhb_physical_teams(jhb_physical_students_list):
    """
    Divides the physical attendees at the Johannesburg campus into teams of 4.
    """
    jhb_physical_teams_list = []
    team = []

    for student in jhb_physical_students_list:
        team.append(student)
        if len(team) == 4:
            jhb_physical_teams_list.append(team)
            team = []

    if team:
        jhb_physical_teams_list.append(team)

    return (jhb_physical_teams_list)


def jhb_teams_file(jhb_physical_teams_list):
    """
    Writes the physical Johannesburg teams into a text file.
    """
    with open("jhb_teams.txt", "w") as file:
        for team_number, team in enumerate(jhb_physical_teams_list, start=1):
            file.write(f"Team {team_number}:\n")
            for student in team:
                file.write(f"  {student}\n")
            file.write("\n")


def nw_campus_students(student_list):
    """
    Filters for attendees at the North West campus from the full student list.
    """
    nw_students = []
    for student in student_list:
        if "Phokeng" in student:
            nw_students.append(student)

    return (nw_students)


def nw_physical_students(nw_students):
    """
    Filters for physical attendees at the North West campus.
    """
    nw_physical_students_list = []
    for student in nw_students:
        if "Physical" in student:
            nw_physical_students_list.append(student)

    return (nw_physical_students_list)


def nw_physical_teams(nw_physical_students_list):
    """
    Divides the physical attendees at the North West campus into teams of 4.
    """
    nw_physical_teams_list = []
    team = []

    for student in nw_physical_students_list:
        team.append(student)
        if len(team) == 4:
            nw_physical_teams_list.append(team)
            team = []

    if team:
        nw_physical_teams_list.append(team)

    return (nw_physical_teams_list)


def nw_teams_file(nw_physical_teams_list):
    """
    Writes the physical teams at the North West campus into a text file.
    """
    with open("nw_teams.txt", "w") as file:
        for team_number, team in enumerate(nw_physical_teams_list, start=1):
            file.write(f"Team {team_number}:\n")
            for student in team:
                file.write(f"  {student}\n")
            file.write("\n")


def get_virtual_students(student_list):
    """
    Filters for the virtual attendees from the full student list.
    """
    virtual_campus = []
    for student in student_list:
        if "Virtual" in student:
            virtual_campus.append(student)

    return (virtual_campus)


def virtual_teams(virtual_campus):
    """
    Divides the virtual attendees into teams of 4.
    """
    virtual_teams_list = []
    team = []

    for student in virtual_campus:
        team.append(student)
        if lean(team) == 4:
            virtual_teams_list.append(team)
            team = []

    if team:
        virtual_teams_list.append(team)

    return (virtual_teams_list)


def virtual_teams_file(virtual_teams_list):
    """
    Writes the virtual teams into a text file
    """
    with open("vr_teams.txt", "w") as file:
        for team_number, team in enumerate(virtual_teams_list, start=1):
            file.write(f"Team {team_number}:\n")
            for student in team:
                file.write(f"  {student}\n")
            file.write("\n")


if __name__ == '__main__':
    students = student_list()

    dbn_students = dbn_campus_students(students)
    physical_dbn_students = dbn_physical_students(dbn_students)
    dbn_teams = dbn_physical_teams(physical_dbn_students)
    dbn_teams_file(dbn_teams)
