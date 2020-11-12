import { Routes } from "@angular/router";
import { AlunoComponent } from "./Aluno/Aluno-component";
import { NewAlunoComponent } from "./Aluno/new-Aluno/new-Aluno.component";
import { ProfessorComponent } from "./Professor/Professor-component";
import { NewProfessorComponent } from "./Professor/new-Professor/new-Professor.component";
import { CursoComponent } from "./Curso/Curso-component";
import { NewCursoComponent } from "./Curso/new-Curso/new-Curso.component";
import { AulaComponent } from "./Aula/Aula-component";
import { NewAulaComponent } from "./Aula/new-Aula/new-Aula.component";


export const ROUTES:Routes = [
    {path:'Aluno',component:AlunoComponent},
    {path:'new-Aluno',component:NewAlunoComponent},
    {path:'Professor',component:ProfessorComponent},
    {path:'new-Professor',component:NewProfessorComponent},
    {path:'Curso',component:CursoComponent},
    {path:'new-Curso',component:NewCursoComponent},
    {path:'Aula',component:AulaComponent},
    {path:'new-Aula',component:NewAulaComponent},

]