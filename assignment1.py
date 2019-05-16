import mysql.connector
import os
import pybedtools
import pysam

__author__ = 'Gerry'

##
## Concept:
## TODO
##


class Assignment1:
    
    def __init__(self):
        ## Your gene of interest
        self.gene = "PDXK"  

    
    def download_gene_coordinates(self, genome_reference, file_name):   # hg38
        ## TODO concept
        
        print("Connecting to UCSC to fetch data")
        
        ## Open connection
        cnx = mysql.connector.connect(host='genome-mysql.cse.ucsc.edu', user='genomep', passwd='password', db=genome_reference)
        
        ## Get cursor
        cursor = cnx.cursor()
        
        ## Build query fields
        query_fields = ["refGene.name2",
                        "refGene.name",
                        "refGene.chrom",
                        "refGene.txStart",
                        "refGene.txEnd",
                        "refGene.strand",
                        "refGene.exonCount",
                        "refGene.exonStarts",
                        "refGene.exonEnds"]
        
        ## Build query
        query = "SELECT DISTINCT %s from refGene" % ",".join(query_fields) # WHERE!!! -> DICT!!
        
        ## Execute query
        cursor.execute(query)
        
        ## Write to file
        ## TODO this may need some work 
        with open(file_name, "w") as fh:
            for row in cursor:
                fh.write(str(row) + "\n")
    
            
        ## Close cursor & connection
        cursor.close()
        cnx.close()
        
        print("Done fetching data")
        
    def get_coordinates_of_gene(self):  # machbar
        ## Use UCSC file
        print("todo")
        
    def get_gene_symbol(self):  # HILFE: Was ist das?
        print("todo")
                        
    def get_sam_header(self):   # pysam
        print("todo")
        
    def get_properly_paired_reads_of_gene(self):    #pysam
        print("todo")
        
    def get_gene_reads_with_indels(self):    ### ab hier nicht mehr
        print("todo")
        
    def calculate_total_average_coverage(self):   # Bedtools
        print("todo")
        
    def calculate_gene_average_coverage(self):  # Bedtools
        print("todo")
        
    def get_number_mapped_reads(self):      
        print("todo")

    def get_region_of_gene(self):
        print("todo")
        
    def get_number_of_exons(self):          #
        print("ads")
    
    
    def print_summary(self):
        
        print("Print all results here")
    
    
def main():
    print("Assignment 1")
    assignment1 = Assignment1()
    #assignment1.download_gene_coordinates('hg38', 'testfile1')
    assignment1.print_summary()
    
    
    print("Done with assignment 1...")
    
        
if __name__ == '__main__':
    main()
    
    
