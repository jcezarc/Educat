import { Routes } from "@angular/router";
import { AlunoComponent } from "./Aluno/Aluno-component";
import { NewAlunoComponent } from "./Aluno/new-Aluno/new-Aluno.component";
import { ProfessorComponent } from "./Professor/Professor-component";
import { NewProfessorComponent } from "./Professor/new-Professor/new-Professor.component";
import { AulaComponent } from "./Aula/Aula-component";
import { NewAulaComponent } from "./Aula/new-Aula/new-Aula.component";
import { PresencaComponent } from "./Presenca/Presenca-component";
import { NewPresencaComponent } from "./Presenca/new-Presenca/new-Presenca.component";


export const ROUTES:Routes = [
    {path:'Aluno',component:AlunoComponent},
    {path:'new-Aluno',component:NewAlunoComponent},
    {path:'Professor',component:ProfessorComponent},
    {path:'new-Professor',component:NewProfessorComponent},
    {path:'Aula',component:AulaComponent},
    {path:'new-Aula',component:NewAulaComponent},
    {path:'Presenca',component:PresencaComponent},
    {path:'new-Presenca',component:NewPresencaComponent},

]