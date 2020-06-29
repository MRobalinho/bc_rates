# https://fastapi.tiangolo.com/tutorial/
# https://github.com/leogregianin/bancocentralbrasil

# With hypercorn installed ASGI frameworks (or apps) can be served via
# Hypercorn via the command line,
# $ cd C:\Users\manuel.robalinho\Google Drive\Trab_Academicos\Python\API
# $ hypercorn api_bc_rates:app

# look at http://127.0.0.1:8000/

from fastapi import FastAPI

import bc.bancocentral
from bc.bancocentral import AcessarBancoCentral
from bc.bancocentral import Inflacao, Poupanca, Cambio, Selic, cleanContent
import datetime


app = FastAPI(title="Robalinho FastAPI example to Exchange rate")

@app.get("/")
async def root():

	#Para buscar os dados do câmbio como o valor do dólar para compra e para venda:
	cambio = Cambio()
	cambio.get_dolar_compra()
	cambio.get_dolar_venda()
	
	# Para buscar os dados da taxa Selic atual:
	selic = Selic()
	selic.get_selic_real()
	
	# tax rates
	cambio = Cambio()
	selic = Selic()
	
	# date and time
	now = datetime.datetime.now()
	
	items = {"Today:": now.strftime("%Y-%m-%d %H:%M:%S"),
			"USD buy PTAX:": cambio.get_dolar_compra_ptax(),
			"USD sell PTAX": cambio.get_dolar_venda_ptax(),
			"USD buy ": cambio.get_dolar_compra(),
			"USD sell ": cambio.get_dolar_venda_ptax(),
			"EUR buy PTAX": cambio.get_euro_compra_ptax(),
			"EUR sell PTAX": cambio.get_euro_venda_ptax(),		
			"EUR buy ": cambio.get_euro_compra(),
			"EUR sell": cambio.get_euro_venda(),	
			"Selic goal ": selic.get_selic_meta(),
			"Selic real": selic.get_selic_real()			
			}
	print('-----------------------------------------------------------')
	print("Exchange rates:", now.strftime("%Y-%m-%d %H:%M:%S"))
	print('-----------------------------------------------------------')
	print(u'Dólar compra PTAX: %s' % cambio.get_dolar_compra_ptax())
	print(u'Dólar venda PTAX: %s' % cambio.get_dolar_venda_ptax())
	print(u'Dólar compra: %s' % cambio.get_dolar_compra())
	print(u'Dólar venda: %s' % cambio.get_dolar_venda())
	print(u'Euro compra PTAX: %s' % cambio.get_euro_compra_ptax())
	print(u'Euro venda PTAX: %s' % cambio.get_euro_venda_ptax())
	print(u'Euro compra: %s' % cambio.get_euro_compra())
	print(u'Euro venda: %s' % cambio.get_euro_venda())
	print(u'Selic meta: %s' % selic.get_selic_meta())
	print(u'Selic real: %s' % selic.get_selic_real())
	
	return {"api_answer": items}

