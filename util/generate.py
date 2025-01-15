from ensurepip import bootstrap
from openai import OpenAI


client = OpenAI(api_key="KEY")


class Generate():
    def __init__(self):
        pass


    async def moderate(self, content: str) -> bool:
        try:
            moderation_response = client.moderations.create(input=content)
            cooked = moderation_response.results[0].flagged

            return cooked
        except Exception as e:
            print(e)
            return True


    async def generate(self, personality: str, content: str) -> str:
        if not await self.moderate(content):
            try:
                response = client.chat.completions.create(model="gpt-4o-mini",
                                                          messages=[
                                                              {"role": "system",
                                                               "content": personality},
                                                              {"role": "user", "content": content},
                                                          ],
                                                          max_tokens=200,
                                                          temperature=1)

                generation = response.choices[0].message.content
            except Exception as e:
                generation = e
        else:
            generation = "Your message was flagged as inappropriate by our internal Jodiebytes. You're cooked bro, you're cooked."


        return generation
