from html2image import Html2Image

def convertor(save_as, unit_name, word, speaking_word, example1_translate, example1_sentence, example2_translate, example2_sentence):

    hti = Html2Image()

    html = f"""
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Auto Filler</title>
        <link rel="stylesheet" href="main.css">
    </head>
    <body>
    
        <div class="head_div container">
            <div class="headdiv_1">
                <b>Destinition</b>
                <i><br>Vocabulary</i>
            </div>
    
            <div class="headdiv_2">
                <b>B1</b>
            </div>
    
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
    
        <div class="mano1 container">
            <p>{example2_translate}</p>
            <p class="mano1_misol">{example2_sentence}</p>
        </div>
    
    </body>
    </html>
    
    """


    css = """ 

    .container{
        margin-left: 40px;
    }
    .head_div{
        width: 100%;
        height: 170px;
        display: flex;
    }
    
    .headdiv_1{
        width: 400px;
        height: 100%;
        display: block;
    }
    
    .headdiv_1 b{
        font-size: 80px;
        font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    }
    
    .headdiv_1 i{
        font-size: 50px;
    }
    
    .headdiv_2{
        width: 65%;
        height: 100%;
    }
    
    .headdiv_2 b{
        font-size: 160px;
        color: rgb(3, 221, 3);
        margin-left: 30px;
        font-family:'Franklin Gothic Medium'
    }
    
    .headdiv_3 p{
        font-size:50px;
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
        color: rgb(3, 221, 3);
    }
    
    .mano1 p{
        font-size: 35px;
    }
    
    .mano1_misol{
        width: 80%;
        height: 130px;
        margin-left: 10%;
        font-size: 30px;
        font-style: italic;
        margin: none;
    }
    
    """

    hti.screenshot(html_str=html, css_str=css, save_as=f'{save_as}.jpg')

#
# convertor('Unit 3', "board ggame", "/bɔːd ɡeɪm/", "1. stol ustida o'ynaluvchi o'yin", "This is a great board game to play with kids - Bu bolalar bilan o'ynash uchun ajoyib stol o'yini", "2. stol ustida o'ynaluvchi o'yin", "me to play with kids - Bu bolalar bilan o'ynash uchun ajoyib st", "1")