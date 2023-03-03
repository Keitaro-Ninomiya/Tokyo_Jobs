Steps for OCR
#Download and Organize#
1. Choose Year
2. Create Page list /Data_Collection/Index
3. Edit page list: Manually
4. Download Documents /Data_Collection/Download_Image
5. Split page into two /Data_Collection/Split_Page
**Make sure to prepare folders before saving splitted image **

#Insert Department Level info into final dataframe#
1. Create dataframe for storing data /Data_Collection/Split_Department

#Create directories
1. Create seperate directories for each department and offices.
/Data_Collection/Create_Directories

#Split into Office Level#
1. Detect starting location of a office /Data_Collection/Split_Office/Code
2. Crop images into office level and save to directory /Data_Collection/Split_Office/Code2

##Split into position level: -1937#
#1. Detect starting location of a office /Data_Collection/Split_Position1

-----------------------------------------------------------------------
#
##Split into unit level: 1937-1942#
#1. Detect starting location of a office /Data_Collection/Split_Position2
#
##Split into unit level: 1943-#
#1. Detect starting location of a office /Data_Collection/Split_Position3
#

#Extract Data#
1. Extract data /Data_Collection/Extract Data