from api.users_api import UsersAPI

def test_to_create_user(api_client):

    user_api = UsersAPI(api_client)

    response = user_api.to_create_user_account()

    assert response.status == 200

def test_get_userDetails(api_client):
    user_api = UsersAPI(api_client)
    
    response = user_api.get_user_information()
    assert response.status == 200