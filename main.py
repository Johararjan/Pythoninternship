import typer
import smtplib
app=typer.Typer()

@app.command()
def enter(sender: str, receivers:str, password:str, subject:str, body:list[str]):
            #in the above input prompt enter your google account application specific password for more details please read the
            # readme.txt file
            server = smtplib.SMTP('smtp.gmail.com', 587)
            message = f'subject:{subject}\n\n{body}'
            server.starttls()
            server.login(sender, password)
            print('login successfull')
            server.sendmail(sender, receivers, message)
            print("email sent successfully")


if __name__=="__main__":
    app()
