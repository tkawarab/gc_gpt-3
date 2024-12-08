import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

#engine_type="text-davinci-002"
def question(type,temperature,top_p,presence_penalty,frequency_penalty,text,max_tokens):
        global engine_type
        global prompt
        if type=="1":
                engine_type="gpt-4"
                prompt = text
                logprobs = 1
        elif type=="2":
                engine_type="content-filter-alpha"
                prompt = "<|endoftext|>"+text+"\n--\nLabel:"
                logprobs = 10
        response = openai.ChatCompletion.create(
                model=engine_type,
                messages=[{"role": "user", "content":prompt}]
                #prompt=prompt,
                #temperature=float(temperature),
                #max_tokens=int(max_tokens),
                #top_p=float(top_p),
                #frequency_penalty=float(frequency_penalty),
                #presence_penalty=float(presence_penalty),
                #logprobs=logprobs
                ##stop=["\n", " Human:", " AI:"]
        )
        if type=="1":
                dict = openai.ChatCompletion.to_dict(response)     
                res = dict["choices"][0]["message"]["content"]           
                return res
        elif type=="2":
                return check_logprobes(response)

def check_logprobes(response):
    output_label = response["choices"][0]["text"]
    # This is the probability at which we evaluate that a "2" is likely real
    # vs. should be discarded as a false positive
    toxic_threshold = -0.355

    if output_label == "2":
        # If the model returns "2", return its confidence in 2 or other output-labels
        logprobs = response["choices"][0]["logprobs"]["top_logprobs"][0]

        # If the model is not sufficiently confident in "2",
        # choose the most probable of "0" or "1"
        # Guaranteed to have a confidence for 2 since this was the selected token.
        if logprobs["2"] < toxic_threshold:
            logprob_0 = logprobs.get("0", None)
            logprob_1 = logprobs.get("1", None)

            # If both "0" and "1" have probabilities, set the output label
            # to whichever is most probable
            if logprob_0 is not None and logprob_1 is not None:
                if logprob_0 >= logprob_1:
                    output_label = "0"
                else:
                    output_label = "1"
            # If only one of them is found, set output label to that one
            elif logprob_0 is not None:
                output_label = "0"
            elif logprob_1 is not None:
                output_label = "1"

            # If neither "0" or "1" are available, stick with "2"
            # by leaving output_label unchanged.

    # if the most probable token is none of "0", "1", or "2"
    # this should be set as unsafe
    if output_label not in ["0", "1", "2"]:
        output_label = "2"

    return output_label

#ret = question("What is required for a car to start?")
#print(ret)
