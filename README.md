# Social-Networking-App
Constraints

· Use any database of your choice

· You are free to design Request/Response fields/formats

· User Login/Signup

· Users should be able to login with their email and password (email should be case

· insensitive)

· User should be able to sign up with their email only (no OTP verification required; valid email format is sufficient)

· Except signup and login every API’s should be called for authenticated users only1

· Develop API for following functionalities:

· API to search other users by email and name (paginate up to 10 records per page).

o If search keyword matches exact email, then return user associated with the email.

o If the search keyword contains any part of the name, then return a list of all users.

Eg:- Amarendra, Amar, aman, Abhirama are three users and if users search with "am" then all these users should be shown in the search result because "am" substring is part of all these names.

c. There will be only one search keyword that will search either by name or email.

2. API to send/accept/reject friend request

3. API to list friends (list of users who have accepted friend request)

4. List pending friend requests (received friend request)

5. Users can not send more than 3 friend requests within a minute.