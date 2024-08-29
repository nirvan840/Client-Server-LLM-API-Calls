# DaSHLab Assignment 2024 [(Assignment)](https://docs.google.com/document/d/1oK0p87q-WvWZB3XpIarPaVZF3DQUhFqfxLy2yW__mEg/pub?urp=gmail_link#h.39v2ctm6mmq)
#### _- Nirvan Patil (2022AAPS1250G)_
#### _- 31st Aug. 2024_
&nbsp;

# Development Assignment [(DaSH Repo)](https://github.com/DaSH-Lab-CSIS/DaSH-Lab-Assignment-2024/blob/main/DevelopmentAssignment/README.md)

## Level 1: API Calls
_Make a script that makes API calls to an LLM API (like gemma, grok). <br> The script should take input from a text file and save the received responses in a .json file._

### <b> <i> Choice of LLM API: **Groq** </b> </i>
* Extensive, easy-to-read documentation when compared to Gemma.
* Support of multiple models and agent calling.
* Faster output speeds and low latency.

   
### <b> <i> Code Explained </b> </i>
* `API_script.py`: Python script to read and store input as required.
  * 1 additional **command line argument** can be passed which is used as **model_choice**
  * Reads from **input.txt** and stores output in **output.json**
* `API_class.py`: Python code for **APIcall** class.
  * **LLM Parameters:** API_Key, model_name (default: "Gemma2 9B"), stop_token (default: None), <br>
    context_size (default: 1024), temperature (default: 0.5), top_p (default: 1) can be <br>
    defined by the user while instantiating an object.
  * **input_filename** and **output_filename** can be specified while calling the object.

<small> _Note: All lines of `input.txt` file are treated as the prompt to the LLM_. <small><br>
<small> _Note: `output.json` file overridden for each new response._ <small>


### <b> <i> Theory of LLM Parameters </b> </i>
<details>
   <summary> <i> Details </i> </summary>
   
   ##### Why Use top_p?
   * **Diversity in Output**: By adjusting top_p, you can control the diversity of the generated text.
   * Lower top_p values make the output more focused and repetitive, while higher values increasee <br>
     diversity but may introduce more randomness.
   ##### Temperature
   * [What is Temp Doing?](https://www.youtube.com/watch?v=YjVuJjmgclU)
     * Small Temp (say 0.5) -> initial logits: [2,1,0.5] -> logits/Temp = [4,2,1] => Clearly the bigger <br>
       probability got bigger by more margin.
     * Big t (say 2) -> [2,1,0.5] -> [1,0.5,0.25] => All probabilities got closer
   * The temperature parameter in large language models (LLMs) is a key hyperparameter that controls the <br>
     randomness or creativity of the model's outputs during text generation**. It affects how the model samples <br>
     from the probability distribution of possible next tokens.
   ##### Temp VS top_p
   * Temp -> Increases random sampling ( more Temp = less random )
   * top_p -> Restricts choices of model ( more top_p = more choices for sampling )
   ##### Stop token
   * stop = stop token corresponding to halting text generation
     
</details>

### <b> <i> References for the section </b> </i>
* [JSON Output](https://github.com/groq/groq-api-cookbook/blob/main/tutorials/json-mode-social-determinants-of-health/SDOH-Json-mode.ipynb)
* [Groq Playground](https://console.groq.com/playground)
* [Groq Documentation](https://console.groq.com/docs/quickstart)
* [Getting Started with Groq API](https://www.youtube.com/watch?v=S53BanCP14c)


&nbsp;

## Level 2: Client Server

### <b> <i> Theory of Client-Server Model </b> </i>
<details>
   <summary> <i> Details </i> </summary>

   #### Domain Name System (DNS)
   
   1. **Problem with IP Addresses:**
      - Every device connected to the internet is identified by a unique IP address, which is a numerical label like `192.168.1.1` for IPv4 or a more complex string like `2001:0db8:85a3:0000:0000:8a2e:0370:7334` 
        for IPv6.
      - However, remembering these numbers is not practical for most people. Imagine trying to remember the IP address for every website you visit!
   
   2. **Domain Names:**
      - To make things easier, domain names were introduced. Domain names are human-readable addresses like `www.google.com`, which are easier to remember and use.
      - Domain names are hierarchical and usually consist of a top-level domain (TLD) like `.com`, `.org`, or `.edu`, followed by a second-level domain (like `google` in `google.com`).
   
   3. **DNS as a Solution:**
      - The Domain Name System (DNS) acts as a translator or a phonebook for the internet.
      - When you type a domain name into your web browser, your computer requests a DNS server to find the IP address associated with that domain name.
   
   4. **How DNS Works:**
      - **DNS Query:** When you enter a domain name (e.g., `www.example.com`), your computer first checks its local DNS cache to see if it already knows the IP address. If not, it sends a DNS query to a DNS 
         resolver (usually provided by your ISP).
      - **DNS Resolver:** The resolver checks its cache. If it doesn't find the answer, it starts hierarchically querying other DNS servers, starting from the root DNS servers.
      - **Root, TLD, and Authoritative DNS Servers:**
        - **Root Servers:** Direct the resolver to the appropriate top-level domain (TLD) server.
        - **TLD Servers:** These direct the resolver to the authoritative DNS server for the specific domain (e.g., `example.com`).
        - **Authoritative DNS Server:** This server provides the actual IP address associated with the domain name.
      - **IP Address Returned:** Once the IP address is found, it's sent back to your computer, and your browser can then connect to the website using that IP address.
   
   5. **Dynamic IP Addresses:**
      - IP addresses can change, especially with dynamic IPs used by most ISPs. The DNS system is designed to handle this by allowing domain owners to update their DNS records with new IP addresses, ensuring 
        that users can still reach their websites.
   
   6. **Why DNS is Important:**
      - DNS makes the internet user-friendly by allowing us to use easy-to-remember domain names instead of complex IP addresses.
      - It also provides a level of abstraction, allowing websites to change servers or IP addresses without affecting the end-user experience.
   
   In summary, DNS is like the internet's directory service, translating human-readable domain names into machine-readable IP addresses, making it possible for us to access websites easily without needing to        remember numerical IP addresses.
   
</details>

### <b> <i> References for the section </i> </b>
* [Client-Server Model](https://www.geeksforgeeks.org/client-server-model/)
* [Domain Name System (DNS)](https://www.geeksforgeeks.org/domain-name-system-dns-in-application-layer/)


&nbsp;

## Level 3: Dockerization


&nbsp;
# Transformers, ViT & SAM 
* Research summary present in respective .md files in the `Research Folder`
* Includes learnings, references, new techniques, etc..


