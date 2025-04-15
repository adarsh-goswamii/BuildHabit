import json
import httpx
from urllib import parse


class LeetCode:
    url = "https://leetcode.com/graphql/"

    def get_leetcode_contributions(self, username: str):
        query = """
           query userProfileCalendar($username: String!, $year: Int) {
                matchedUser(username: $username) {
                    userCalendar(year: $year) {
                        submissionCalendar
                    }
                }
           }
        """
        variables = {"username": username}

        response = httpx.get(f"{LeetCode.url}?{parse.urlencode({"query": query, "variables": json.dumps(variables)})}")

        return response.json()


if "__main__" == __name__:
    sol = LeetCode()
    sol.get_leetcode_contributions("Adarsh_Goswami")
