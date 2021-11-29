import app = require("teem");

class IndexRoute {
	public async index(req: app.Request, res: app.Response) {
		let paises: any[];

		await app.sql.connect(async (sql) => {
			paises = await sql.query("SELECT id_pais, nome_pais FROM renewableenergy.pais");
		});

		res.render("index/index", {
			paises: paises
		});
	}

	public async filtrar(req: app.Request, res: app.Response) {
		const id_pais = parseInt(req.query["id_pais"] as string);

		if (!id_pais) {
			res.json([]);
			return;
		}

		let dados: any[];

		await app.sql.connect(async (sql) => {
			dados = await sql.query("SELECT ano, producao FROM renewableenergy.pais_producao WHERE id_pais = ?", [id_pais]);
		});

		res.json(dados);
	}
}

export = IndexRoute;
