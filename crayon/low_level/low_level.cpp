#include <cpr/cpr.h>

#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include <string>

using json = nlohmann::json;
using namespace std;

class Ville {
  string nom;
  int code_postal;
  int prix_metre2;

 public:
  Ville(string nom_, int code_postal_, int prix_metre2_)
      : nom{nom_}, code_postal{code_postal_}, prix_metre2{prix_metre2_} {}
  friend std::ostream& operator<<(std::ostream& out, const Ville& v) {
    return out << v.nom << " ; code postale: " << v.code_postal
               << " ; prix par m2: " << v.prix_metre2;
  }
  Ville(json data) {
    nom = data["nom"];
    code_postal = data["code postale"];
    prix_metre2 = data["prix par m2"];
  }
};

class Local {
  string nom;
  std::unique_ptr<Ville> ville;
  int surface;

 public:
  Local(string nom_, json ville_, int surface_)
      : nom{nom_}, ville{std::make_unique<Ville>(ville_)}, surface{surface_} {}
  friend std::ostream& operator<<(std::ostream& out, const Local& l) {
    return out << l.nom << " ; ville: " << *l.ville
               << " ; surface: " << l.surface;
  }
  Local(json data) {
    nom = data["nom"];
    ville = make_unique<Ville>(data["ville"]);
    surface = data["surface"];
  }
};

auto main() -> int {
  const auto v = Ville(data);
  const auto l = Local(
      json::parse(cpr::Get(cpr::Url{"http://localhost:8000/Local/2"}).text));
  std::cout << "Local: " << l << std::endl;
  return 0;
}

/*class Ville
{
    string nom ;
    int code_postal;
    int prix_metre2;

    public:
        Ville(string nam, int code_p, int prix_m2) : nom{nam},
code_postal{code_p}, prix_metre2{prix_m2} {} friend std::ostream&
operator<<(std::ostream& out, const Ville& v) { return out << v.nom << " / " <<
v.code_postal << " / " << v.prix_metre2;
        }
        Ville(json data){

        cout << data["nom"] << " / " << data["code_postal"] << " / " <<
data["prix_metre2"]<<endl;
        }

};

auto main() -> int {
    cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/ville/1"});
    json data = json::parse(Get(r.txt));
    //ville=Ville(json data) ;
//std::cout <<"ville :"<< Ville{"Toulouse", 31000, 350} << " \n";
std::cout << "ville" << Ville <<std::endl;
return 0;
}*/
