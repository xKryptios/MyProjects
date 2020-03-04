#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover file.raw");
        return 1;
    }

    char *infile = argv[1];
    FILE *inptr = fopen(infile,"r");
    if (inptr == NULL)
    {
        printf("could not open %s", infile);
        return 1;
    }

    BYTE buffer[512];
    int counter = 0;
    char filename[8];
    FILE *img = NULL;
    bool jpeg_found = false;

    // loop on every block of data on infile
    while (fread(&buffer,sizeof(buffer),1,inptr))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //indicate first jpeg header found
            jpeg_found = true;

            // close the jpeg file for subsequent jpegs
            if( counter > 0 )
            {
                fclose(img);
            }

            // create file name
            sprintf(filename, "%03i.jpg", counter);

            //open new image file
            img = fopen(filename,"w");

            //check if image created sucessfully
            if (img == NULL)
            {
                printf("Unable to create JPG %s",filename);
                return 1;
            }

            counter++;
        }

        //starts writing each block if first jpeg found
        if (jpeg_found)
        {
            fwrite(&buffer,sizeof(buffer),1,img);
        }
    }

    fclose(img);
    fclose(inptr);
}