# Client data creation and encryption

## Purpose:  
### Create fake data to test our platform recommendation algorithms.
### Establish encryption standards and practices.

&nbsp;
## Running this module:
If a key does not exist run `$ python lock.py` in the command line to generate a new key.

To create new client data and/or view existing client data the generate_client_data.py script can be run with options in the command line.
1. `$ python generate_client_data.py`
    - This will create all new client data and read the newly created file
2. `$ python generate_client_data.py --gen True`
    - This will create new client data
3. `$ python generate_client_data.py --view_data True`
    - This will read and decrypt the existing client data in `data.csv`

&nbsp;
## This module is responsible for the following:
1. Create fake client names and phone numbers
2. Encrypt PII client data
3. Generate client platform preferences
4. Generate client genre preferences
5. View client decrypted client data

&nbsp;
## Additional resources:
> Client Data Creation and Encryption.pptx 
>   - Data creation flow chart
>   - Explanation of threshold calculations used in
>       - Platform creation 
>       - Genre data creation


> For detailed information each function is commented, see all python files in this directory:
>   - const.py
>   - generate_client_data.py
>   - lock.py

> Client faker documentation
>   - https://faker.readthedocs.io/en/master/

> Fernet encryption documentation
>   - https://cryptography.io/en/latest/fernet/