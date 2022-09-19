from html2image import Html2Image


def convertor(save_as, unit_name, word, speaking_word, example1_translate, example1_sentence, example2_translate,
              example2_sentence):
    hti = Html2Image(output_path='C:/Users/Student/AppData/IqrorjonCoder/Vs-Code/Auto-filler/autofiller/static/')

    if example2_translate == "" and example2_sentence == "":

        html = f"""

<div class="body">

    <div class="head_div container">
        <img src="C:/Users/Student/AppData/IqrorjonCoder/Vs-Code/Auto-filler/autofiller/static/des_name.png" alt="Destinition name" class="destinition_image">
        <div class="headdiv_3">
            <p>{unit_name}</p>
        </div>
    </div>

    <div class="text_name">
        <p>{word}</p>
    </div>
    
    <div class="text_speaking">
        <h1>{speaking_word}</h1>
    </div>

    <div class="mano1 container">
        <p>{example1_translate}</p>
        <p class="mano1_misol">{example1_sentence}</p>
    </div>

</div>
   
        """
        css = """ 
.body{
    width: 100%;
    height: 100%;
    background-color: white;
    margin: none;
}

.container{
    margin-left: 40px;
    width: auto;
    height: auto;
}
.head_div{
    width: 100%;
    height: 170px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.destinition_image{
    width: 500px;
    height: 120px;
}

.headdiv_3 p{
    font-size:50px;
    margin-right: 80px;
    font-family: sans-serif;
}

.text_name{
    width: 100%;
    height: 200px;
    margin-top: 30px;
    display: flex;
    justify-content:center;
    align-items: center;
    font-family: sans-serif;
}

.text_name p{
    font-size: 160px;
}

.text_speaking{
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 25px;
    color: #7db521;
    font-family: sans-serif;
}


.mano1 p{
    font-size: 30px;
}

.mano1_misol{
    width: 80%;
    height: 110px;
    margin-left: 10%;
    font-size: 25px;
    font-style: italic;
    margin: none;
}


            """

        hti.screenshot(html_str=html, css_str=css, save_as=f'{save_as}.jpg', size=(1700, 800))
        # print(save_as, unit_name, word, speaking_word, example1_translate, example1_sentence, example2_translate,
        #       example2_sentence)

    else:
        html = f"""
<div class="body">

    <div class="head_div container">
        <img src="C:/Users/Student/AppData/IqrorjonCoder/Vs-Code/Auto-filler/autofiller/static/des_name.png" alt="Destinition name" class="destinition_image">
        <div class="headdiv_3">
            <p>{unit_name}</p>
        </div>
    </div>

    <div class="text_name">
        <p>{word}</p>
    </div>
    
    <div class="text_speaking">
        <h1>{speaking_word}</h1>
    </div>

    <div class="mano1 container">
        <p>{example1_translate}</p>
        <p class="mano1_misol">{example1_sentence}</p>
    </div>

    <div class="mano2 container">
        <p>{example2_translate}</p>
        <p class="mano2_misol">{example2_sentence}</p>
    </div>

</div>
            """

        css = """ 


.body{
    width: auto;
    height: auto;
    background-color: white;
}

.container{
    margin-left: 40px;
    width: auto;
    height: auto;
}
.head_div{
    width: 100%;
    height: 170px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.destinition_image{
    width: 500px;
    height: 120px;
}

.headdiv_3 p{
    font-size:50px;
    margin-right: 80px;
    font-family: sans-serif;
}

.text_name{
    width: 100%;
    height: 200px;
    margin-top: 30px;
    display: flex;
    justify-content:center;
    align-items: center;
    font-family: sans-serif;
}

.text_name p{
    font-size: 160px;
}

.text_speaking{
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 25px;
    color: #7db521;
    font-family: sans-serif;
}

.mano1 p{
    font-size: 30px;
}

.mano1_misol{
    width: 80%;
    height: 110px;
    margin-left: 10%;
    font-size: 25px;
    font-style: italic;
    margin: none;
}

.mano2 p{
    font-size: 30px;
}
.mano2_misol{
    width: 80%;
    height: 110px;
    margin-left: 10%;
    font-size: 25px;
    font-style: italic;
    margin: none;
}
    
    """

        hti.screenshot(html_str=html, css_str=css, save_as=f'{save_as}.jpg', size=(1700, 1000))
        # print(save_as, unit_name, word, speaking_word, example1_translate, example1_sentence, example2_translate,
        #       example2_sentence)

# convertor("sava_as", 'Unit 2', 'hello', 'he:ll', '1. salom', 'this is first example', '4352',
#           'fghsdgh')
