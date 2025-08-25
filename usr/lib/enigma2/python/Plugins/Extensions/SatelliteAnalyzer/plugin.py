# plugin.py
from Plugins.Plugin import PluginDescriptor
from Screens.MessageBox import MessageBox
from Plugins.Extensions.SatelliteAnalyzer.SatelliteAnalyzer import SatelliteAnalyzer


PLUGIN_VERSION = "1.0"

def main(session, **kwargs):
    session.open(SatelliteAnalyzer)

def Plugins(**kwargs):
    return PluginDescriptor(
        name="SatelliteAnalyzer",
        description=f"Show all information about the current channel (Version {PLUGIN_VERSION})",
        where=PluginDescriptor.WHERE_PLUGINMENU,
        icon="satellite.png",
        fnc=main,
    )