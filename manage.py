from flask.cli import FlaskGroup


from my_app import app,db
from my_app.catalog.models import Discos


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    db.session.add(Discos(nme_disco="We are Reactive",artista="Hohpe",estilo="Indie",ano_lancto=2022,quantidade=500))
    db.session.add(Discos(nme_disco="Time of the Oath",artista="Helloween",estilo="Metal",ano_lancto=1996,quantidade=2000))
    db.session.add(Discos(nme_disco="Hero Amaurer",artista="Tilt",estilo="HardCore",ano_lancto=1996,quantidade=9450))
    db.session.add(Discos(nme_disco="Out of Bounds",artista="No Fun at all",estilo="HardCore",ano_lancto=1995,quantidade=9450))


    db.session.commit()


if __name__ == "__main__":
    cli()
