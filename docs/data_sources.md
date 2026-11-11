# Data Sources

## Introduction

For the first version of the project, I want to focus on MBTI and Enneagram. These will be the two frameworks used in the initial proof of concept, before adding Big Five, Human Design and Color Analysis.

I am looking for information that explains each framework and its different types, rather than datasets containing social media posts labelled with personality types. The user will provide their own assessment results, so the purpose of the knowledge base is to give the LLM information about the characteristics and concepts associated with those results. The LLM should not try to determine someone's personality from their writing.

I also want to keep track of where the information comes from and whether it can actually be included in the retrieval database. This is important because a source can be useful for research without necessarily allowing its content to be copied into a vector database.

## MBTI

For MBTI, I want to cover the four preference pairs: Extraversion–Introversion, Sensing–Intuition, Thinking–Feeling and Judging–Perceiving. Their combinations form the 16 MBTI types. I am also interested in type dynamics and the cognitive processes associated with the framework.

### Selected corpus source

**Myers–Briggs Type Indicator — Wikipedia**

https://en.wikipedia.org/wiki/Myers%E2%80%93Briggs_Type_Indicator

This article gives an overview of the MBTI framework, including its four preference pairs, its connection to Jung's theory of psychological types, type dynamics and some of the criticism surrounding the model.

I selected it as an initial corpus source because the article is available under the Creative Commons Attribution-ShareAlike 4.0 license. This allows reuse under the conditions of that license, including attribution and ShareAlike requirements when adapting the material.

The article is useful for understanding the overall framework, but it does not provide detailed descriptions for all 16 types. I will need to investigate an additional source for that part before considering the MBTI corpus complete.

The article was last edited on 8 August 2026. I accessed it on 11 November 2026.

### Additional reference sources

**Myers & Briggs Foundation — The 16 MBTI Personality Types**

https://www.myersbriggs.org/my-mbti-personality-type/the-16-mbti-personality-types/home.htm

This is useful because it provides descriptions of all 16 MBTI types. I will use it as a reference when checking how the types are described in the official framework.

However, the page contains excerpts from a copyrighted publication by The Myers-Briggs Company. Its copyright policy specifically restricts copying its publications into stored databases or retrieval systems without prior written authorization. I will therefore not add the full page to the RAG corpus unless the necessary permission is obtained.

**Myers & Briggs Foundation — The Processes of Type Dynamics**

https://www.myersbriggs.org/unique-features-of-myers-briggs/type-dynamics-processes/

I will use this page as a reference for the dominant, auxiliary, tertiary and inferior processes. These are relevant to the cognitive-function approach, but I will distinguish the theoretical framework from claims that have strong empirical support.

## Enneagram

For Enneagram, I want to focus initially on the nine core types and the motivations, fears and desires associated with each of them. I am also interested in wings and the relationships between types, but I will keep these as possible extensions rather than treating them as equally well-supported parts of the model.

One thing I need to consider is that different Enneagram authors and schools do not always use exactly the same descriptions. For the initial corpus, I will use one consistent interpretation and record which source it comes from rather than combining different versions without distinction.

### Selected corpus source

**Enneagram of Personality — Wikipedia**

https://en.wikipedia.org/wiki/Enneagram_of_Personality

This article provides an overview of the Enneagram and a summary of the nine types. It includes concepts such as basic fears, basic desires, passions, virtues, wings and the relationships between types.

The article explains that its table of type characteristics is based primarily on the work of Don Richard Riso and Russ Hudson, together with material from Charles Tart. I will use this as the reference for the initial Enneagram representation, while keeping in mind that other Enneagram traditions may describe some aspects differently.

The article is available under the Creative Commons Attribution-ShareAlike 4.0 license, so it can be included in the initial corpus provided that the attribution and license requirements are respected.

The article was last edited on 11 July 2026. I accessed it on 11 November 2026.

### Additional reference sources

**Alexander, M., and Schnipke, B. — The Enneagram: A Primer for Psychiatry Residents (2020)**

https://doi.org/10.1176/appi.ajp-rj.2020.150301

This article, published in the *American Journal of Psychiatry Residents' Journal*, provides an overview of the Enneagram and summarizes the nine types, including their basic fears and desires.

I will use it as an academic reference to compare the descriptions in the corpus. It is not currently selected as a raw retrieval source because I have not established a license that allows its full text to be copied into the database.

**Hook, J. N., Hall, T. W., Davis, D. E., Van Tongeren, D. R., and Conner, M. — The Enneagram: A Systematic Review of the Literature and Directions for Future Research (2021)**

https://doi.org/10.1002/jclp.23097

I will use this review to understand the research evidence and limitations of the Enneagram. The authors reviewed 104 independent samples and found mixed evidence for reliability and validity. They also noted that there is limited research supporting some secondary parts of the theory, such as wings and movement between types.

This source is important because I do not want the project to present the Enneagram as a scientifically established personality measurement system. It will be used as an interpretive framework based on the user's own assessment result.

## Data Collection and Organization

For the initial version, I will collect the two selected corpus sources and keep the original material separate from the processed documents used for retrieval.

I also want to preserve the source information when processing the documents. This means keeping the title, author or organization, URL, publication or last-edited date, retrieval date and license information. That way, when the LLM retrieves information, it should be possible to identify where that information came from.

For sources that allow reuse under a license, I will keep the required attribution and record any modifications made during processing. For sources that are only used for reference, I will keep their bibliographic information without copying their full content into the retrieval database.

## Initial Scope

The initial proof of concept will use MBTI and Enneagram. The user will provide their own results for both frameworks, and the LLM will use the knowledge base to interpret those results when answering a question.

At this stage, I will focus on the basic framework concepts and the nine Enneagram types. The MBTI source collection still needs an additional reusable source for detailed descriptions of all 16 types.

After this initial version, I can extend the knowledge base with Big Five/BFAS, Human Design and 16-season Color Analysis. I will keep these frameworks separate because they describe different aspects of a person and should not all be interpreted in the same way.