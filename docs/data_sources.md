# Data Sources

## Introduction

For the initial version of the project, I want to focus on MBTI and Enneagram. These will be the two frameworks used in the first experiments.

I am looking for sources that describe the frameworks and their different types, rather than datasets containing social media posts labelled with personality types. The user will provide their own assessment results, and the LLM will use the information in the knowledge base to answer questions based on those results.

I have separated the sources into two groups. The first contains material that I can use as a basis for the initial knowledge base. The second contains official and academic references that I can use to check terminology, understand the frameworks and document their limitations.

## 1. MBTI

### Corpus source

**Myers–Briggs Type Indicator — Wikipedia**

[Article](https://en.wikipedia.org/wiki/Myers%E2%80%93Briggs_Type_Indicator)

[Selected revision](https://en.wikipedia.org/w/index.php?title=Myers%E2%80%93Briggs_Type_Indicator&oldid=1368276565)

[Revision history](https://en.wikipedia.org/w/index.php?title=Myers%E2%80%93Briggs_Type_Indicator&action=history)

This article explains the four preference pairs: Extraversion–Introversion, Sensing–Intuition, Thinking–Feeling and Judging–Perceiving. It also covers the historical background of the framework, cognitive functions, type dynamics and some of the criticism surrounding its reliability and validity.

I will use it as an introductory source for the MBTI concepts. However, it does not provide a complete collection of detailed descriptions for all 16 types, so an additional source will be needed if I want to represent each type individually in the knowledge base.

**Source information**

- Author: Wikipedia contributors
- Last revision: 8 August 2026
- Revision ID: 1368276565
- Retrieved: 11 November 2026
- License: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0), as stated in the article footer.

The text can be reused under the license conditions. This includes providing attribution, linking to the original article and license, indicating modifications and respecting the ShareAlike requirement for adapted material. I will use the article text, not assume that its images and other media have the same license.

### Additional references

**Myers & Briggs Foundation — The 16 MBTI Personality Types**

[Official descriptions of the 16 types](https://www.myersbriggs.org/my-mbti-personality-type/the-16-mbti-personality-types/home.htm)

This page provides descriptions of all 16 types and is useful for checking the terminology and the way each type is presented in the official MBTI framework.

I will keep it as a reference rather than copying its text into the retrieval database. The Myers-Briggs publisher's copyright policy restricts reproduction of its publications in stored databases and retrieval systems without prior written authorization.

**Myers & Briggs Foundation — Type Dynamics: Processes**

[Type Dynamics and Processes](https://www.myersbriggs.org/unique-features-of-myers-briggs/type-dynamics-processes/)

This page explains the dominant, auxiliary, tertiary and inferior processes. It is relevant because I want to investigate whether cognitive functions should be represented separately from the four-letter type result.

These official pages are useful references, but their full text will not be included in the corpus unless the applicable reuse permissions are established.

## 2. Enneagram

### Corpus source

**Enneagram of Personality — Wikipedia**

[Article](https://en.wikipedia.org/wiki/Enneagram_of_Personality)

[Selected revision](https://en.wikipedia.org/w/index.php?title=Enneagram_of_Personality&oldid=1363671110)

[Revision history](https://en.wikipedia.org/w/index.php?title=Enneagram_of_Personality&action=history)

This article is more useful for the initial prototype because it contains a structured table describing all nine Enneagram types.

The table includes characteristic roles, ego fixations, basic fears, basic desires, passions, virtues and the relationships between types under stress and security. The article also covers the three triads, wings and instinctual subtypes.

The table is based primarily on Don Richard Riso and Russ Hudson's *Understanding the Enneagram*, together with material from Charles Tart. The article also notes that other Enneagram authors may disagree with some of these descriptions.

I will use the nine-type table and the relevant sections about triads, wings and connections between types as the initial basis for the Enneagram knowledge base.

**Source information**

- Author: Wikipedia contributors
- Last revision: 11 July 2026
- Revision ID: 1363671110
- Retrieved: 11 November 2026
- License: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0), as stated in the article footer.

The same attribution and ShareAlike requirements apply here. I will also preserve the selected revision so that the source used in the experiments can be identified later.

### Additional references

**Alexander, M., and Schnipke, B. (2020) — The Enneagram: A Primer for Psychiatry Residents**

[Article](https://doi.org/10.1176/appi.ajp-rj.2020.150301)

Published in the *American Journal of Psychiatry Residents' Journal*, Volume 15, Issue 3, on 6 March 2020.

This article provides an overview of the nine types, including their basic fears, desires and characteristic behaviour patterns. It also discusses wings, stress and security patterns and instinctual variants.

I will use it as an academic reference to compare the descriptions in the knowledge base. I have not established a license that allows the article's full text to be copied into the retrieval database, so it will remain a reference source.

**Hook, J. N., Hall, T. W., Davis, D. E., Van Tongeren, D. R., and Conner, M. (2021) — The Enneagram: A Systematic Review of the Literature and Directions for Future Research**

[Article](https://doi.org/10.1002/jclp.23097)

Published in the *Journal of Clinical Psychology*, Volume 77, Issue 4, pages 865–883.

This systematic review examines the empirical research on the Enneagram across 104 independent samples. The authors found mixed evidence for reliability and validity. They also point out that there is limited empirical support for some additional aspects of the theory, including wings and movement between types.

I will use this article to document the scientific limitations of the framework. It is not intended to provide the type descriptions used for retrieval.

## 3. Data Collection

For the initial version, the two Wikipedia articles are the selected corpus sources. I will preserve the original text and the source information separately from the processed documents used for retrieval.

When processing the articles, I want to keep the framework and source information attached to the extracted content. This will make it possible to identify whether a retrieved description belongs to MBTI or Enneagram and where that information originally came from.

For Wikipedia material, I will preserve the original article URL, revision ID, authorship attribution, license and any changes made during processing. I will also keep the original source text unchanged so that I can compare it with the processed version.

The official MBTI pages and academic publications will remain reference material until their reuse conditions are established.

## 4. Initial Scope

The first knowledge base will focus on the four MBTI preference pairs and the nine Enneagram types. I will also investigate how much additional information about cognitive functions, wings and relationships between types is useful for answering personalized questions.

The two frameworks will remain distinguishable in the knowledge base. I do not want to present their categories as equivalent measurements or assume that every characteristic associated with a type is scientifically established.

The next step will be to identify an additional reusable source for detailed descriptions of all 16 MBTI types. This is the main gap in the current source collection.

After the initial experiments, I plan to investigate adding Big Five/BFAS, Human Design and 16-season Color Analysis as separate frameworks.

### Additional corpus source

**Personality Data Project — 16 Personality Types**

[All 16 personality types](https://www.personalitydata.org/16-types/personality-types)

[Example: INTJ profile](https://www.personalitydata.org/16-types/intj)

This source provides individual descriptions for all 16 four-letter personality types. Each type has its own page with an overview, general principles and an explanation of the four letters. Additional pages cover strengths and weaknesses, extended subtypes, relationships and careers.

I will use the overview pages to fill the gap in the MBTI source collection, since the Wikipedia article does not provide detailed profiles for all 16 types.

The descriptions are based on the 16-type Jungian model. I will treat them as secondary interpretive descriptions rather than official MBTI definitions. I will also avoid using the population statistics and demographic charts as personality characteristics, since these are based on separate self-reported survey data.

**Source information**

- Organization: Personality Data Project (PersonalityData.org)
- Named contributor: Ellie Simmonds, MSc, is listed on the INTJ profile; the project's About page also lists her among the psychologists who helped develop its personality assessments.
- Format: Individual HTML pages for the 16 types
- Coverage: General descriptions, type principles and four-letter preference explanations
- License: Creative Commons Attribution 4.0 International (CC BY 4.0), except where otherwise noted
- Retrieved: 11 November 2026

I can reuse and adapt the licensed content provided that I give appropriate attribution to PersonalityData.org and link to the original source and license. I will preserve the original URLs in the processed documents.
