# Tesseract-OCR Using Python "ocrmypdf" Package.

Using ocrmypdf, We can convert the PDF / TIFF / JPEG objects as text searchable. I have tried to convert upto 100MB of file size with
Max DPI as 300. And most of the OCR's doesn't support this much bigger size of DPI and Memory. Python OCRMYPDF will be able to process
such huge files sucessfully.

Note: Pricing for this solution is just for an EC2 instance. We can have some alerting mechanism to mark autoscaling group desired
      instance as 1, when an then the file reached to S3. And configure all the following into a bootstrap script of the EC2 Instance.

Step - 1:

        Create an S3 Bucket "ocrmydocuments" in AWS.
        Create directories "ocr_documents" & "non_ocr_documents"
        Upload the PDF / TIFF / JPEG into "ocr_documents" directory.
        
Step - 2:

        Create an IAM Role, Which will allow access to the above defined S3 Bucket.
        
Step - 3:

        Create EC2 Instance from AWS Console using "Ubuntu 18.04" AMI. (In a Private Subnet)

Step - 4:

        On SSH into the EC2 instance,
        
        * Make sure python3 is available. If not, Install Python 3.6 or above.
        * sudo apt-get -y update
        * sudo apt-get -y install \
                          ghostscript \
                          icc-profiles-free \
                          liblept5 \
                          libxml2 \
                          pngquant \
                          python3-cffi \
                          python3-distutils \
                          python3-pkg-resources \
                          python3-reportlab \
                          qpdf \
                          tesseract-ocr \
                          zlib1g
        * Get the PIP installable,
                          wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py
        * export PATH=$HOME/.local/bin:$PATH
        * python3 -m pip install --user ocrmypdf

Step - 5:
        
        After all the above installations, We will get the command line interface to convert the document 
        into text searchable format. Following are some example commands,
        
        ocrmypdf --output-type pdf --image-dpi 300 <<Source File Name>>.tiff <<Destination File Name>>.pdf
        ocrmypdf --output-type pdf --image-dpi 300 <<Source File Name>>.jpeg <<Destination File Name>>.pdf
        ocrmypdf --output-type pdf <<Source File Name>>.pdf <<Destination File Name>>.pdf
        
Note: The attached PDF can accept the file name as input parameter and it GET the file from S3 and after transformation it PUT
      the file back into s3://ocrmydocuments/ocr_documents
        
Note: "ocrmypdf" also can be used with AWS Lambda. But this approach not supporting the transformation of TIFF and JPEG. But it is
      Sucessfully working with PDF's. To invoke the Lambda function by configuring the Events on S3 Object PUT in the bucket.
