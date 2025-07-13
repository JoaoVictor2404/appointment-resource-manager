def test_create_resource(client):
    client.post("/users/", json={"email":"u@u.com","password":"pwd"})
    token = client.post("/token", data={"username":"u@u.com","password":"pwd"}).json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    res = client.post("/resources/", json={"name":"Sala 1","type":"Sala"}, headers=headers)
    assert res.status_code == 200 and res.json()["name"] == "Sala 1"
