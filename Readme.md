This tool is designed to simplify the process of authorizing a HubSpot OAuth application and obtaining refresh tokens.

## Installation
In order to run this tool you must have python installed, get it [here](https://www.python.org/downloads/).

First, we need to create a virtual environment where our dependencies will be installed. You can create one with
```bash
python -m venv venv
```
Then activate the environment with
```bash
venv\Scripts\activate (on windows)
```
Since the projects has a couple dependencies we must install those.
```bash
pip install -r requirements.txt
```
## Configuration
The project has a config.json5 file which should be filled with the credentials of your OAuth application.
```json5
{
    // the client id of the app
    client_id: '',
    // the client secret of the app
    client_secret: '',
    // the permission scopes that the app will request
    scopes: [
        ''
    ]
}
```
## Use
Now the project is ready to be run, you can start it using the command
```bash
flask --app oauth_authorize.py run
```
This will open the OAuth authorization page in your browser and listen for the redirect callback.
Once the app is authorized it will trade the authorization token for an refresh token that can be used to generate access tokens to access the HubSpot api.
The refresh token will be displayed after redirection.
