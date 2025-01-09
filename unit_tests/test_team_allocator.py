#!/usr/bin/env python3
"""
Unit tests for the Team Allocator.
"""
import unittest
from features.team_allocator import *


class TestTeamAllocator(unittest.TestCase):
    """Tests for the team_allocator module."""

    def test_data_base(self):
        database = student_list()
        self.assertEqual(type(database), type(['list']))


    def test_dbn_campus(self):
        test_database = ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual']

        durban_campus = dbn_campus_students(test_database)
        self.assertEqual(durban_campus, ['zanelejhb2022-2may-durbanvirtual'])

    
    def test_cpt_campus(self):
        test_database = ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual']

        cape_campus = cpt_campus_students(test_database)
        self.assertEqual(cape_campus, ['ddhaaljhb2022-2may-capetownvirtual'])


    def test_jhb_campus(self):
        test_database = ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual']

        joburg_campus = jhb_campus_students(test_database)
        self.assertEqual(joburg_campus, ['zakithikhdbn2022-4april-johannesburgphysical-seat3'])


    def test_nw_campus(self):
        test_database = ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
    'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual']

        phokeng_campus = nw_campus_students(test_database)
        self.assertEqual(phokeng_campus, ['thandohdbn2022-4april-phokengphysical-seat3'])

    
    def test_dbn_physical_students(self):
        test_database = ['zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'zaneleJHB2022 - 2 May - Durban Physical - seat 3', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3']
        
        physical_students = dbn_physical_students(test_database)
        self.assertEqual(physical_students, ['zanelejhb2022-2may-durbanphysical-seat3', 'yenzilejhb2022-2may-durbanphysical-seat3'])


    def test_cpt_physical_students(self):
        test_database = ['zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'zaneleJHB2022 - 2 May - Cape Town Physical - seat 3', 'yenzileJHB2022 - 2 May - Cape Town Physical - seat 3']
        
        physical_students = cpt_physical_students(test_database)
        self.assertEqual(physical_students, ['zanelejhb2022-2may-capetownphysical-seat3', 'yenzilejhb2022-2may-capetownphysical-seat3'])


    def test_jhb_physical_students(self):
        test_database = ['zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'zaneleJHB2022 - 2 May - Johannesburg Physical - seat 3', 'yenzileJHB2022 - 2 May - Johannesburg Physical - seat 3']
        
        physical_students = jhb_physical_students(test_database)
        self.assertEqual(physical_students, ['zanelejhb2022-2may-johannesburgphysical-seat3', 'yenzilejhb2022-2may-johannesburgphysical-seat3'])


    def test_nw_physical_students(self):
        test_database = ['zaneleJHB2022 - 2 May - Durban Virtual',
    'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'zaneleJHB2022 - 2 May - Phokeng Physical - seat 3', 'yenzileJHB2022 - 2 May - Phokeng Physical - seat 3']
        
        physical_students = nw_physical_students(test_database)
        self.assertEqual(physical_students, ['zanelejhb2022-2may-phokengphysical-seat3', 'yenzilejhb2022-2may-phokengphysical-seat3'])


    def test_durban_even_teams(self):
        test_database = ['zakithikhDBN2022 - 4 April - Durban Physical - seat 3', 'thembisiweDBN2022 - 4 April - Durban Physical - seat 5',
        'thenjisiweDBN2022 - 4 April - Durban Physical - seat 6', 'thethelelileDBN2022 - 4 April - Durban Physical - seat 7', 
        'thembiDBN2022 - 4 April - Durban Physical - seat 4', 'thobekilDBN2022 - 4 April - Durban Physical - seat 8', 'kgothatshoDBN2022 - 4 April - Durban Physical - seat 9',
        'thatoDBN2022 - 4 April - Durban Physical - seat 1']

        dbn_even_teams = dbn_physical_teams(test_database)
        self.assertEqual(dbn_even_teams, [['zakithikhdbn2022-4april-durbanphysical-seat3', 'thembisiwedbn2022-4april-durbanphysical-seat5',
        'thenjisiwedbn2022-4april-durbanphysical-seat6', 'thetheleliledbn2022-4april-durbanphysical-seat7'],
        ['thembidbn2022-4april-durbanphysical-seat4', 'thobekildbn2022-4april-durbanphysical-seat8', 'kgothatshodbn2022-4april-durbanphysical-seat9',
        'thatodbn2022-4april-durbanphysical-seat1']])


    def test_durban_odd_teams(self):
        test_database = ['zakithikhDBN2022 - 4 April - Durban Physical - seat 3', 'thembisiweDBN2022 - 4 April - Durban Physical - seat 5',
        'thenjisiweDBN2022 - 4 April - Durban Physical - seat 6', 'thethelelileDBN2022 - 4 April - Durban Physical - seat 7', 
        'thembiDBN2022 - 4 April - Durban Physical - seat 4', 'thobekilDBN2022 - 4 April - Durban Physical - seat 8', 'kgothatshoDBN2022 - 4 April - Durban Physical - seat 9',
        'thatoDBN2022 - 4 April - Durban Physical - seat 1', 'zuzumuziDBN2022 - 4 April - Durban Physical - seat 18', 'kgothatshoDBN2022 - 4 April - Durban Physical - seat 19',
        'josephineDBN2022 - 4 April - Durban Physical - seat 11']

        dbn_odd_teams = dbn_physical_teams(test_database)
        self.assertEqual(dbn_odd_teams, [['zakithikhdbn2022-4april-durbanphysical-seat3', 'thembisiwedbn2022-4april-durbanphysical-seat5',
        'thenjisiwedbn2022-4april-durbanphysical-seat6', 'thetheleliledbn2022-4april-durbanphysical-seat7'],
        ['thembidbn2022-4april-durbanphysical-seat4', 'thobekildbn2022-4april-durbanphysical-seat8', 'kgothatshodbn2022-4april-durbanphysical-seat9',
        'thatodbn2022-4april-durbanphysical-seat1'], ['zuzumuzidbn2022-4april-durbanphysical-seat18', 'kgothatshodbn2022-4april-durbanphysical-seat19',
        'josephinedbn022-4april-durbanphysical-seat11']])


    def test_capetown_even_teams(self):
        test_database = ['zakithikhDBN2022 - 4 April - Cape Town Physical - seat 3', 'thembisiweDBN2022 - 4 April - Cape Town Physical - seat 5',
        'thenjisiweDBN2022 - 4 April - Cape Town Physical - seat 6', 'thethelelileDBN2022 - 4 April - Cape Town Physical - seat 7', 
        'thembiDBN2022 - 4 April - Cape Town Physical - seat 4', 'thobekilDBN2022 - 4 April - Cape Town Physical - seat 8', 'kgothatshoDBN2022 - 4 April - Cape Town Physical - seat 9',
        'thatoDBN2022 - 4 April - Cape Town Physical - seat 1']

        cpt_even_teams = cpt_physical_teams(test_database)
        self.assertEqual(cpt_even_teams, [['zakithikhdbn2022-4april-capetownphysical-seat3', 'thembisiwedbn2022-4april-capetownphysical-seat5',
        'thenjisiwedbn2022-4april-capetownphysical-seat6', 'thetheleliledbn2022-4april-capetownphysical-seat7'],
        ['thembidbn2022-4april-capetownphysical-seat4', 'thobekildbn2022-4april-capetownphysical-seat8', 'kgothatshodbn2022-4april-capetownphysical-seat9',
        'thatodbn2022-4april-capetownphysical-seat1']])


    def test_capetown_odd_teams(self):
        test_database = ['zakithikhDBN2022 - 4 April - Cape Town Physical - seat 3', 'thembisiweDBN2022 - 4 April - Cape Town Physical - seat 5',
        'thenjisiweDBN2022 - 4 April - Cape Town Physical - seat 6', 'thethelelileDBN2022 - 4 April - Cape Town Physical - seat 7', 
        'thembiDBN2022 - 4 April - Cape Town Physical - seat 4', 'thobekilDBN2022 - 4 April - Cape Town Physical - seat 8', 'kgothatshoDBN2022 - 4 April - Cape Town Physical - seat 9',
        'thatoDBN2022 - 4 April - Cape Town Physical - seat 1', 'zuzumuziDBN2022 - 4 April - Cape Town Physical - seat 18', 'kgothatshoDBN2022 - 4 April - Cape Town Physical - seat 19',
        'josephineDBN2022 - 4 April - Cape Town Physical - seat 11']

        cpt_odd_teams = cpt_physical_teams(test_database)
        self.assertEqual(cpt_odd_teams, [['zakithikhdbn2022-4april-capetownphysical-seat3', 'thembisiwedbn2022-4april-capetownphysical-seat5',
        'thenjisiwedbn2022-4april-capetownphysical-seat6', 'thetheleliledbn2022-4april-capetownphysical-seat7'],
        ['thembidbn2022-4april-capetownphysical-seat4', 'thobekildbn2022-4april-capetownphysical-seat8', 'kgothatshodbn2022-4april-capetownphysical-seat9',
        'thatodbn2022-4april-capetownphysical-seat1'], ['zuzumuzidbn2022-4april-capetownphysical-seat18', 'kgothatshodbn2022-4april-capetownphysical-seat19',
        'josephinedbn022-4april-capetownphysical-seat11']])


    def test_johannesburg_even_teams(self):
        test_database = ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5',
        'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 
        'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'thobekilDBN2022 - 4 April - Johannesburg Physical - seat 8', 'kgothatshoDBN2022 - 4 April - Johannesburg Physical - seat 9',
        'thatoDBN2022 - 4 April - Johannesburg Physical - seat 1']

        jhb_even_teams = jhb_physical_teams(test_database)
        self.assertEqual(jhb_even_teams, [['zakithikhdbn2022-4april-johannesburgphysical-seat3', 'thembisiwedbn2022-4april-johannesburgphysical-seat5',
        'thenjisiwedbn2022-4april-johannesburgphysical-seat6', 'thetheleliledbn2022-4april-johannesburgphysical-seat7'],
        ['thembidbn2022-4april-johannesburgphysical-seat4', 'thobekildbn2022-4april-johannesburgphysical-seat8', 'kgothatshodbn2022-4april-johannesburgphysical-seat9',
        'thatodbn2022-4april-johannesburgphysical-seat1']])


    def test_johannesburg_odd_teams(self):
        test_database = ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5',
        'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 
        'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'thobekilDBN2022 - 4 April - Johannesburg Physical - seat 8', 'kgothatshoDBN2022 - 4 April - Johannesburg Physical - seat 9',
        'thatoDBN2022 - 4 April - Johannesburg Physical - seat 1', 'zuzumuziDBN2022 - 4 April - Johannesburg Physical - seat 18', 'kgothatshoDBN2022 - 4 April - Johannesburg Physical - seat 19',
        'josephineDBN2022 - 4 April - Johannesburg Physical - seat 11']

        jhb_odd_teams = jhb_physical_teams(test_database)
        self.assertEqual(jhb_odd_teams, [['zakithikhdbn2022-4april-johannesburgphysical-seat3', 'thembisiwedbn2022-4april-johannesburgphysical-seat5',
        'thenjisiwedbn2022-4april-johannesburgphysical-seat6', 'thetheleliledbn2022-4april-johannesburgphysical-seat7'],
        ['thembidbn2022-4april-johannesburgphysical-seat4', 'thobekildbn2022-4april-johannesburgphysical-seat8', 'kgothatshodbn2022-4april-johannesburgphysical-seat9',
        'thatodbn2022-4april-johannesburgphysical-seat1'], ['zuzumuzidbn2022-4april-johannesburgphysical-seat18', 'kgothatshodbn2022-4april-johannesburgphysical-seat19',
        'josephinedbn022-4april-johannesburgphysical-seat11']])


if __name__ == '__main__':
    unittest.main()
