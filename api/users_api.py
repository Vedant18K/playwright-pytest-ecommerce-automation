class UsersAPI:
    def __init__(self , client):
        self.client = client
        
    def to_create_user_account(self):
        payload = {
            "name": "Test",
            "email": "test@system.com",
            "password": "Sample@123",
            "title":"Mr",
            "birth_date":"22",
            "birth_month":"04",
            "birth_year":"2002",
            "firstname":"First Name",
            # "middlename":"Middle Name",
            "lastname":"Last Name",
            "company":"Company",
            "address1": "Address 1 ",
            "address2": "Address 2",
            "country": "India",
            "zipcode":"34521",
            "state": "Maharashtra",
            "city": "Aurangabad",
            "mobile_number":"7538457334"
            }
        return self.client.post("/api/createAccount", payload)
    
    def get_user_information(self):
        payload = {
            "email":"test@system.com"
        }
        return self.client.get("/api/getUserDetailByEmail")