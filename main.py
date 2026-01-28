import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from urllib3 import response

load_dotenv()


def main():
    print("Hello lang chain")
    information = """ 
    Shiva Sanskrit: शिव, IAST: Śiva, Sanskrit: [ɕɪʋɐ] ⓘ, lit. 'The Auspicious One'), also known as Mahadeva (/məˈhɑː ˈdeɪvə/; Sanskrit: महादेव, IAST: Mahādevaḥ, [mɐɦaːd̪eːʋɐh], lit. 'The Great God')[17][18][19] and Hara (Sanskrit: हर, lit. 'The Remover'),[20] is one of the principal deities of Hinduism.[21] He is the Supreme Being in Shaivism, one of the major traditions within Hinduism.[22]

    In the Shaivite tradition, Shiva is the Supreme Lord who creates, protects and transforms the universe.[17][18][19] In the goddess-oriented Shakta tradition, the Supreme Goddess (Devi) is regarded as the energy and creative power (Shakti) and the equal complementary partner of Shiva.[23][24] Shiva is one of the five equivalent deities in Panchayatana puja of the Smarta tradition of Hinduism.[25] Shiva is known as The Destroyer within the Trimurti, the Hindu trinity which also includes Brahma and Vishnu.[6][26]

    Shiva has many aspects, benevolent as well as fearsome. In benevolent aspects, he is depicted as an omniscient yogi who lives an ascetic life on Kailasa[6] as well as a householder with his wife Parvati and his two children, Ganesha and Kartikeya. In his fierce aspects, he is often depicted slaying demons. Shiva is also known as Adiyogi (the first yogi), regarded as the patron god of yoga, meditation and the arts.[27] The iconographical attributes of Shiva are the serpent king Vasuki around his neck, the adorning crescent moon, the holy river Ganga flowing from his matted hair, the third eye on his forehead (the eye that turns everything in front of it into ashes when opened), the trishula or trident as his weapon, and the damaru. He is usually worshiped in the aniconic form of lingam.[7]

    Though associated with Vedic deity Rudra, Shiva may have non-Vedic roots,[28] evolving as an amalgamation of various older non-Vedic and Vedic deities, including the Rigvedic storm god Rudra who may also have non-Vedic origins,[29] into a single major deity.[30] Shiva is a pan-Hindu deity, revered widely by Hindus in India, Nepal, Bangladesh, Sri Lanka and Indonesia (especially in Java and Bali).[31]
    """
    summary_template = """ 
    Give the information {information} about a god i want to explore:
    1. Short summary
    2. 2 interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
    )
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
