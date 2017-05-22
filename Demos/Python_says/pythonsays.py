# -*- coding: utf-8 -*-

'''

Python says

A program that generates Verilog code and design, verify, build and load the code using APIO

Made by Julián Caro Linares

jcarolinares@gmail.com

CC-BY-SA

'''

#Libraries
import os
import subprocess
import time

import apio
from apio.managers.scons import SCons
from apio.managers.project import Project

#Local archives
import hardwaretemplates


#Variables
path="." #By the time the path it must be the root of the project. Apio needs that (Scons().verify doesn't have a path parameter)
fpgaboard="icezum"
pythonsays_memo="[PYTHON SAYS]: " #Keyword that defines the outputs generated by pythonsays

N_counter=[25,24,23,22,21,20,19,18]

#APIO CALLING FUNCTIONS

class FPGA_engine(object):

    def __init__(self):
        self.board="icezum"
        self.scons_engine=SCons(".") #Ahora mismo da problemas
        self.project=Project()


    def config_fpga(self):
        print("\n\n"+pythonsays_memo+"Calling APIO FPGA Board Setup (PROJECT)"+"\n\n")

        #project=Project()
        self.project.create_ini(self.board, path, False)

        #apio.managers.scons.Project.create_ini(fpgaboard_name, path, False) #Another lower level option
        return True

    def verify_hdl(self):
        #subprocess.call('echo "\n\nCalling APIO Verify (SCONS)"' ,shell=True)
        print("\n\n"+pythonsays_memo+"Calling APIO Verify (SCONS)"+"\n\n")

        #scons_engine=SCons()

        self.scons_engine.verify()
        return True

    def build_hdl(self):
        print("\n\n"+pythonsays_memo+"BUILDING CIRCUIT"+"\n\n")

        #Apio building calling (SCONS)

        #scons_engine=SCons()
        '''
        scons_engine.__init__()#Not needed
        scons_engine.build({
            'board': board,
            'fpga': fpga,
            'size': size,
            'type': type,
            'pack': pack
        })
        '''


        self.scons_engine.build({ #Details extracted from boards.json and fpgas.json Device argument must be 0
            'board': "icezum",
            'fpga': "iCE40-HX1K-TQ144",
            'size': "1k",
            'type': "hx",
            'pack': "tq144"
        })

        return True

    def upload_hdl(self):
        print("\n\n"+pythonsays_memo+"UPLOADING CIRCUIT"+"\n\n")

        #scons_engine=SCons()

        self.scons_engine.upload({ #Details extracted from boards.json and fpgas.json Device argument must be 0
            'board': "icezum",
            'fpga': "iCE40-HX1K-TQ144",
            'size': "1k",
            'type': "hx",
            'pack': "tq144"
        }, 0)
        return True

    def verify_build_upload(self): #This functions calls apio verify and apio upload, synthesizing the circuit in the process (build)
        print("\n\n"+pythonsays_memo+"VERIFY_BUILD_UPLOAD"+"\n\n")

        if self.verify_hdl()==True:
            if self.upload_hdl()==True:
                return True



#Main execution
def main():

    #FPGA generation and apio init
    fpga=FPGA_engine()

    if fpga.config_fpga()==True:
        print("\n\n"+pythonsays_memo+"FPGA CONFIGURATION COMPLETED")
        #pins_inputoutput=[21]+range(119,116-1,-1)
        #countertemplate.generate_counter(template_path="hardware_templates/counter_template.txt",output_file="counter.v",MSB=3,N=22,increment=1,pininout=pins_inputoutput)


    # # #Counter generation test
    # for MSB in range(1,9,1):
    #
    #     #Generation of verilog file
    #     #countertemplate.generate_counter("hardware_templates/counter_template.txt","counter.v",N,5)
    #     pins_inputoutput=[21]+range(119,119-MSB,-1)
    #     hardwaretemplates.generate_counter(template_path="hardware_templates/counter_template.txt",output_file="counter.v",MSB=MSB,N=20,increment=1,pininout=pins_inputoutput)
    #
    #
    #     #Circuits generations and fpga upload
    #     if fpga.verify_build_upload()==True:
    #         print("\n\n"+pythonsays_memo+"CIRCUIT UPLOADED WITH N: "+str(MSB)+" bits\n\n")
    #
    #         time.sleep(10)


    #Secuence notes generator (Music generator)
    for octave in range (11):
        #Generation of verilog file
        hardwaretemplates.generate_sec_notes(template_path="../hardware_templates/sec_notes.txt",octave=octave,duration=500)

        #Circuits generations and fpga upload
        if fpga.verify_build_upload()==True:
            print("\n\n"+pythonsays_memo+"CIRCUIT UPLOADED WITH OCTAVE: "+str(octave)+"\n\n")

            time.sleep(25)



if __name__ == "__main__":
 main()
