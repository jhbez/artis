from flask import current_app

def inject_env():
##import pdb; pdb.set_trace()
    return dict(
        artis = current_app.config.get("ARTIS", False),
        facebook = current_app.config.get("FACEBOOK", False),
        px500 = current_app.config.get("PX500", False),
        instagram = current_app.config.get("INSTAGRAM", False),
    )