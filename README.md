

# Introduction to python programming and bioinformatics

September 20-24, 2021

Course leader: Courtney Stairs (Dept. of Biology, Lund University) 

courtney.stairs@biol.lu.se


## Location and Time

We will meet from 9-16 with breaks around 1030 and 1430.

All meetings will be held in the B and D Houses of the Biology Building located on Sölvegatan 35. I suggest entering the building from the main entrance on the south side of the building (facing the new LTH tram stop). Once inside, you are on the ‘second floor’ (floor 2), turn left to access the B and D houses. https://maps.app.goo.gl/GDTBdNb1kQpW2FDo8



* B327 Syndpunkten - Conference room on the third floor of House B
* D227 Retina - Second floor of House D
* D107 Etiketten - First floor of House D

For lunch, there is a canteen in the Ecology House that will be open. There are also multiple lunchrooms we will have access to with microwaves. 

The zoom link for all meetings will be: https://lu-se.zoom.us/j/67479512343?pwd=YS9mbDVvV2xKdFUwRVlLSnJNSlNoZz09


## Format & Evaluation

I think that coding is best learned by doing. Therefore there will be very few formal ‘lecturers’ in this course. Instead, we will have guided exercises and tutorials ending in a mini-project for you to complete to apply what you learned. Attendance in mandatory each day to receive credits (3 hp). Evaluation is pass/fail based on participation and completion of the exercises.  


## Schedule at a glance


### Day1: September 20th 2021 

Room B327 Synpunkten



* Personal introductions 
* Introduction to Jupyter Lab
* Basic python tutorial
* Code Discussion
* Debugging exercises
* Hand-in exercises 


### Day2: September 21st 2021 

Room B327 Synpunkten



* Online exercises
* Introduction to biopython
* Biopython - build a fasta parser
* Biopython - e-utilities (API)
* Online exercises
* Hand-in exercise 


### Day3: September 22nd 2021

Room D227 Retina



* Introduction to dataframes and tables with Pandas
* Tour of online databases (EggNOG, NCBI, PFAM, Interpro)
* Local installation of databases
* Local BLAST
* (I will be absent for 30 minutes in the afternoon to give a talk on zoom on metagenomes, lateral gene transfer and anaerobic metabolism in deep-sea Chlamydia. You are welcome to attend)


### Day4: September 23rd 2021

Room D227 Retina



* Local multiple sequence alignments
* Local phylogenetic tools


### Day5: September 23rd 2021

Room D107 Etiketten 



* Project - from sequence to annotation. Combine what you have learned. Write a script or Jupyter notebook to help you annotate an unknown protein locally - that is, do not simply BLAST your sequence using BLAST online. Your workflow should include at least 4 of the following outputs:
    * The protein sequence in a fasta file
    * The taxonomy of the origin of the sequence
    * A small FASTA file of the top 50 related sequences from local database.
        * Challenge: consult the biopython cookbook on how to do a remote look up!
    * A table describing each of the top 50 related sequences. For e.g.,
        * Description of the sequence (annotation)
        * Length in amino acids
        * Organism, other taxonomy?
    * Multiple sequence alignment of your mystery sequence and the top 50 proteins - this should have reformatting FASTA headers for easy reading.
        * Challenge: Worried about identical sequences? Try installing ‘cd-hit’ in your conda environment and learning more about the tool.. 
    * Phylogenetic tree of these 50 proteins (keep the model simple)
        * Challenge: before making the alignment, think about what you would like in your Sequence names. Could taxonomy be helpful? 
