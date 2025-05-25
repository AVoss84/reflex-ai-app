# import asyncio
import reflex as rx
from web_app.backend import chain


class State(rx.State):

    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    def clear_history(self):
        self.chat_history = []

    async def answer(self):

        # Ignore empty or whitespace-only questions
        if not self.question or self.question.strip() == "":
            return
        # Add new chat history tuple
        # set the question to the current input
        # the answer is initially empty
        answer = ""
        self.chat_history.append((self.question, answer))

        # response = chain.invoke(
        #     {"input": self.question},
        #     # config={"callbacks": [StreamingStdOutCallbackHandler()]},
        # )
        print("Question:", self.question)
        # Use the chatbot to get a response.
        response = chain.invoke({"input": self.question})
        answer = response["response"]
        # print("Response:", response)

        # Update the last chat history tuple with the full response.
        self.chat_history[-1] = (
            self.chat_history[-1][0],
            answer,  # replace second tuple element with the full response
        )
        # Clear the question input for the user.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        # for i in range(len(answer)):
        #     # Pause to show the streaming effect.
        #     await asyncio.sleep(0.1)
        #     # Add one letter at a time to the output.
        #     self.chat_history[-1] = (
        #         self.chat_history[-1][0],
        #         answer[: i + 1],
        #     )
        #     yield

    # # Streaming answer function to simulate a chatbot response.
    # async def answer(self):
    #     # Our chatbot is not very smart right now...
    #     answer = "I don't know!"
    #     self.chat_history.append((self.question, ""))

    #     # Clear the question input.
    #     self.question = ""
    #     # Yield here to clear the frontend input before continuing.
    #     yield

    #     for i in range(len(answer)):
    #         # Pause to show the streaming effect.
    #         await asyncio.sleep(0.1)
    #         # Add one letter at a time to the output.
    #         self.chat_history[-1] = (
    #             self.chat_history[-1][0],
    #             answer[: i + 1],
    #         )
    #         yield
