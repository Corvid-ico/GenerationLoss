from PIL import Image
def StartCreation(Title, GenCn, GenMax, Gens, DegreeRotation):
    TotalGenesGenerated = Gens
    OriginTitle = f'./Image_Directory/{Title}.jpeg'
    open_image = Image.open(OriginTitle)

    while (Gens > 0):
        print(f'Image Sub-Gen: {((GenCn *GenMax - Gens)%GenMax)+1} - Gen {((GenCn *GenMax - Gens)//GenMax) +1}')
        
        original_img = Image.open(OriginTitle)# Open the original provided/Gen(ν-1) image
        recreated_img = original_img.convert('RGB')# Convert to RGB
        recreated_img = recreated_img.rotate(DegreeRotation)# Rotate the image by 360/GivenRot
        
        Gens = Gens - 1 #Reduce SUB-Generation count
        OriginTitle = f'./Exported/Raw_Generations/gen{GenCn *GenMax - Gens}.jpeg'#Combine new info for title
        
        recreated_img.save(OriginTitle)# Save the recreated image

        if ((Gens % GenMax) == 0): #On 360 degrees rotation save the Generation
            print(f'Batch {((GenCn*GenMax)//GenMax)-(Gens // GenMax)} out of {GenCn} Exported! \n')
            recreated_img.save(f'./Exported/Indp_Generations/gen{GenCn *GenMax - Gens}.jpeg')