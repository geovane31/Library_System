from datetime import datetime

# Biblioteca
books = []
students = []
authors = []
loans = []
book_id_counter = 1 #Iniciar o contador de ID dos livros
author_id_counter = 1 #Iniciar o contador de ID dos autores
aluno_id_counter = 1 #Iniciar o contador de ID dos alunos

def createBook(title, author):
    dataAtual = datetime.now()
    global book_id_counter
    book = { 
      "id": book_id_counter,
      "title": title,
      "author": author,
      "isAvailable": True,
      "created_at": dataAtual,
      "updated_at": dataAtual
  }
    book_id_counter +=1
    return book

def createAuthor(name, dateBirth):
    global author_id_counter
    author = {
      "id": author_id_counter,
      "name": name,
      "dateBirth": dateBirth
  } 
    author_id_counter += 1
    return author

def createStudent(name,dateBirth,email):
    global aluno_id_counter
    aluno = {
        "id": aluno_id_counter,
        "name": name,
        "dateBirth": dateBirth,
        "email": email,
        "borrowed_books": []
    }
    aluno_id_counter += 1
    return aluno

def getBook(title_or_id):
    if len(books) == 0:
        print("--- Não existe livro cadastrado ---")
    else:
        for book in books:
            if str(book["id"]) == title_or_id or book["title"].lower() == title_or_id.lower():
                status = "Disponivel" if book["isAvailable"] else "Emprestado"
                created_at = book["created_at"].strftime("%d/%m/%Y %H:%M:%S")
                print(f"ID: {book['id']} \nTítulo: {book['title']} \nAutor: {book['author']['name']} \nStatus: {status} \nData de Cadastro: {created_at}\n")
                return
        print("Livro não encontrado")

def editBooks(title_or_id):
    for book in books:
        if str(book["id"]) == title_or_id or book["title"].lower() == title_or_id.lower():
            print("--- Livro Encontrado ---")
            print(f"\nID: {book['id']} \nTítulo: {book['title']} \nAutor: {book['author']['name']}\n")
            while True:
                print("O que você deseja editar?")
                print("1 .Título")
                print("2 .Autor")
                print("3 .Sair")

                option = tryInput("Escolha a opção que deseja editar: ")

                if option == 1:
                    new_title = input("Digite o novo título do livro: ")
                    if new_title:
                        book["title"] = new_title
                        book["updated_at"] = datetime.now()
                        print("--- Título atualizado com sucesso! ---")
                        break
                    else: 
                        print("Título não pode ser vazio")

                elif option == 2:
                    new_author = input("Digite o novo autor do livro: ")
                    if new_author:
                        book["author"]["name"] = new_author
                        book["update_at"] = datetime.now()
                        print("--- Autor atualizado com sucesso! ---")
                        break
                    else:
                        print("--- Autor não pode ser vazio ---")
                elif option == 3:
                    break
                else:
                    print("\n--- Opção Inválida, escolha uma das opções ---\n")
            return
    print("Livro Não encontrado")

def deleteBooks(title_or_id):
    global books
    bookDelete = None

    for book in books:
        if str(book["id"]) == title_or_id or book["title"].lower() == title_or_id.lower():
            bookDelete = book
            break

    if bookDelete:
        if confirm(f"Você tem certeza que deseja excluir o livro: {bookDelete['title']} (ID: {bookDelete['id']}) ?"):
            books.remove(bookDelete)
            print("--- Livro excluido com sucesso ---")
        else:
            print("--- Ação Cancelada ---")
    else:
        print("Livro não encontrado")

def listBooks():
    if len(books) == 0:
        print("--- Não existe livro cadastrado ---")
    else:
        for book in books:
            status = "Disponivel" if book["isAvailable"] else "Emprestado"
            created_at = book["created_at"].strftime("%d/%m/%Y %H:%M:%S")
            print(f"\nID: {book['id']} \nTítulo: {book['title']} \nAutor: {book['author']['name']} \nStatus: {status} \nData de Cadastro: {created_at}")

            if "updated_at" in book:
                updated_at = book ["updated_at"].strftime("%d/%m/%Y %H:%M:%S")
                print(f"Ultima atualização: {updated_at}\n")

def listStudent():
    if len(students) == 0:
        print("--- Não existe aluno Cadastrado ---")
    else:
        for student in students:
            borrowed_books = student["borrowed_books"]
            borrowed_titles_date = []
            for book in books:
                if book["id"] in borrowed_books:
                    for loan in loans:
                        if loan["book_id"] == book["id"] and loan["student_id"] == student["id"]:
                            loan_date = loan["loan_date"].strftime("%d/%m/%Y %H:%M:%S")
                            borrowed_titles_date.append(f"{book['title']} (Emprestimo: {loan_date})")
            borrowed_books_str = ', '.join(borrowed_titles_date) if borrowed_titles_date else "Nenhum livro emprestado"
            print(f"\nID: {student['id']} \nNome: {student['name']} \nData de Nascimento: {student['dateBirth'].strftime("%d/%m/%Y")} \nE-mail: {student['email']} \nLivros Emprestados: {borrowed_books_str}")

def editStudents(name_or_id):
    for student in students:
        if str(student["id"]) == name_or_id or student["name"].lower() == name_or_id.lower():
            print("--- Aluno Encontrado ---")
            print(f"\nID: {student['id']} \nNome: {student['name']} \nData de Nascimento: {student['dateBirth'].strftime("%d/%m/%Y")} \nE-mail: {student['email']}\n")
            while True:
                print("O que deseja editar?")
                print("1. Nome")
                print("2. Data de Nascimento")
                print("3. E-mail")
                print("4. Sair")

                option = tryInput("Escolha a opção que deseja editar: ")

                if option == 1:
                    new_students = input("Digite o novo nome do Aluno: ")
                    if new_students:
                        student["name"] = new_students
                        print("--- Nome atualizado com sucesso! ---")
                        break
                    else:
                        print("--- É obrigatório digitar nome ---")
                elif option == 2:
                    new_date = tryDate("Digite a nova data de nascimento DD/MM/AAAA: ")
                    if new_date:
                        student["dateBirth"] = new_date
                        print("--- Data de Nascimento atualizado com sucesso! ---")
                        break
                    else:
                        print("--- Data de Nascimento não pode está em branco")
                elif option == 3:
                    new_email = input("Digite o novo e-mail: ")
                    if new_email:
                        student["email"] = new_email
                        print("--- E-mail Atualizado com sucesso! ---")
                        break
                    else:
                        print("E-mail não pode está em branco")
                elif option == 4:
                    break
                else:
                    print("\n--- Opção Inválida, escolha umas das opções ---\n")
            return
    print("Aluno não encontrado")



def bookAvilable(title_or_id):
    for book in books:
        if str(book["id"]) == title_or_id or book["title"].lower() == title_or_id.lower():
            if book["isAvailable"]:
                print("Livro Disponivel para empréstimo")
                return True
            else:
                print("Livro não está disponível para empréstimo")
                return False
    print("Livro Não encontrado")
    return False

def loanBook(title_or_id, student_identifier):
    book_found = None
    for book in books: 
       if str(book["id"]) == title_or_id or book["title"].lower() == title_or_id.lower():
        book_found = book
        break

    if not book_found:
        print("Livro Não encontrado")
        return False
    if not book_found["isAvailable"]:
        print("O Livro não está disponível para empréstimo")
        return False

    student_found = None
    for student in students:
        if str(student["id"]) == student_identifier or student["name"].lower() == student_identifier.lower():
            student_found = student
            break

    if not student_found:
        print("Aluno não encontrado")
        return False

    loan = {
        "book_id": book["id"],
        "student_id": student["id"],
        "loan_date": datetime.now(),
        "return_date": None
    }
    loans.append(loan)
    book["isAvailable"] = False
    book["updated_at"] = datetime.now()
    student_found["borrowed_books"].append(book_found["id"])
    
    print("--- Empréstimo realizado com sucesso ---")
    return True

def returnBook(title_or_id):
    book_id = None
    for book in books:
        if str(book["id"]) == title_or_id or book["title"].lower() == title_or_id.lower():
            book_id = book["id"]
            break

    if book_id is None:
        print("Livro não encontrado")
        return

    for loan in loans:
        if loan["book_id"] == book_id and loan ["return_date"] is None:
            loan["return_date"] = datetime.now()

            for book in books:
                if book["id"] == book_id:
                    book["isAvailable"] = True
                    book["updated_at"] = datetime.now()

                    for student in students:
                        if student["id"] == loan["student_id"]:
                            student["borrowed_books"].remove(book_id)
                    print(f"--- Empréstimo do livro --- \nID: {book['id']} \nTítulo: {book['title']} \nAutor: {book['author']['name']} \n--- EMPRÉSTIMO FINALIZADO! ---")
                    return
    print("Empréstimo não encontraddo ou já foi devolvido")

def listStudentHistory(student_identifier):
    student_found = None
    for student in students:
        if str(student["id"]) == student_identifier or student["name"].lower() == student_identifier.lower():
            student_found = student
            break
    if not student_found:
        print("Aluno não encontrado")
        return

    found_loans = None
    print(f"\n--- Histórico do Aluno: {student_found['name']} (ID: {student_found["id"]}) ---")
    for loan in loans:
        if loan["student_id"] == student_found["id"]:
            found_loans = True

            book_found = None
            for book in books:
                if book["id"] == loan["book_id"]:
                    book_found = book
                    break

            loan_date = loan["loan_date"].strftime("%d/%m/%Y %H:%M:%S")
            return_date = loan["return_date"].strftime("%d/%m/%Y %H:%M:%S") if loan["return_date"] else "Livro Não Devolvido"

            if book_found:
                
                print(f"\nLivro: {book_found['title']} (ID: {book['id']}) \nData do Empréstimo: {loan_date} \nData de Entrega: {return_date}")
    if not found_loans:
        print("Nenhum empréstimo encontrado para este aluno.")

def bookLoanHistory(book_identifier):
    book_found = None
    for book in books:
        if str(book["id"]) == book_identifier or book["title"].lower() == book_identifier.lower():
            book_found = book
            break
    if not book_found:
        print("Livro não encontrado")
        return

    found_loans = False
    print(f"\n--- (ID: {book['id']}) Título: {book['title']} ---")
    for loan in loans:
        if loan["book_id"] == book_found["id"]:
            found_loans = True

            student_found = None

            for student in students:
                if student["id"] == loan["student_id"]:
                    student_found = student
                    break

            loan_date = loan["loan_date"].strftime("%d/%m/%Y %H:%M:%S")
            return_date = loan["return_date"].strftime("%d/%m/%Y %H:%M:%S") if loan["return_date"] else "Ainda Não Devolvido"

            if student_found:
                print(f"\nEmprestado para Aluno: {student_found['name']} (ID: {student_found["id"]}) \nData do Empréstimo: {loan_date} \nData de Entrega: {return_date}\n")
    if not found_loans:
        print("Nenhum empréstimo registrado para este livro")

def authorTheBook(authorBook):
    if len(books) == 0:
        print("--- Não existe Autor cadastrado ---")
        return
    
    find_book = False
    for book in books:
        if str(book["author"]["name"]).lower() == authorBook.lower():
            find_book = True
            status = "Disponivel" if book["isAvailable"] else "Emprestado"
            created_at = book["created_at"].strftime("%d/%m/%Y %H:%M:%S")
            print(f"\nID: {book['id']} \nTítulo: {book['title']} \nAutor: {book['author']['name']} \nStatus: {status} \nData de Cadastro: {created_at}")
    if find_book == False:
        print("Livro do autor especifico não encontrado")

def deleteStudents(name_or_id):
    global students
    studentDelete = None

    for student in students:
        if str(student["id"]) == name_or_id or student["name"].lower() == name_or_id.lower():
            studentDelete = student
            break

    if studentDelete:
        if confirm(f"Você tem certeza que deseja excluir o livro: {studentDelete['name']} (ID: {studentDelete['id']}) ?"):
            students.remove(studentDelete)
            print("--- Aluno excluido com sucesso ---")
        else:
            print("--- Ação Cancelada ---")
    else:
        print("Aluno não encontrado")

def editAuthor(name_or_id):
    find_author = False
    for author in authors:
        if str(author["id"]) == name_or_id or author["name"].lower() == name_or_id.lower():
            print("--- Autor Encontrado ---")
            print(f"\nID: {author['id']} \nAutor: {author['name']} \nData de Nascimento: {author['dateBirth'].strftime("%d/%m/%Y")}\n")
            
            while True:
                print("O que você deseja editar?")
                print("1. Nome")
                print("2. Data de Nascimento")
                print("3. Sair")

                option = tryInput("Escolha a opção que deseja editar: ")

                if option == 1:
                    new_name = input("Digite novo nome do Autor: ")
                    if new_name:
                        author["name"] = new_name
                        print("--- Nome do autor atualizado com sucesso ---")
                        break
                    else:
                        print("--- Nome não pode ser vazio ---")
                elif option == 2:
                    new_date = tryDate("Digite a nova data de nascimento DD/MM/AAAA: ")
                    if new_date:
                        author["dateBirth"] = new_date
                        print("--- Data de nascimento atualizada com sucesso ---")
                        break
                    else:
                        print("--- Data de nascimento Inválida ---")
                elif option == 3:
                    break
                else:
                    print("--- Opção Inválida, escolha umas das opções ---")
            return
        print("Autor não encontrado")

def listAuthor():
    if len(authors) == 0:
        print("--- Não existe Autor cadastrado ---")
    else:
        for author in authors:
            print(f"\nID: {author["id"]} \nAutor: {author["name"]} \nData de Nascimento: {author['dateBirth'].strftime("%d/%m/%Y")}")

def deleteAutor(name_or_id):
    global authors
    authorDelete = None

    for author in authors:
        if str(author["id"]) == name_or_id or author["name"].lower() == name_or_id.lower():
            authorDelete = author
            break

    if authorDelete:
        if confirm(f"Você tem certeza que deseja excluir o livro: {authorDelete["name"]} (ID: {authorDelete["id"]}) ?"):
            authors.remove(authorDelete)
            for book in books:
                if book["author"]["id"] == authorDelete["id"]:
                    book["author"] = {"name": "Autor Excluído"}
            print("--- Autor excluido com sucesso ---")
        else:
            print("--- Ação Cancelada ---")
    else:
        print("Autor não encontrado")

#Função de repetição ValueError
def tryInput(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("--- Entrada inválida, insira um numero das opções ---")

def tryDate(prompt):
    while True:
        date_input = input(prompt)
        try:
            valid_date = datetime.strptime(date_input, "%d/%m/%Y")
            return valid_date
        except ValueError:
            print("--- Data inválida, insina a data no formato DD/MM/AAAA ---")
# Função de confirmação
def confirm(action):
    response = input(f"{action} (S/N): ").lower()
    return response == 's'

#Funções das condicionais
def cadastrarLivro():
    print("--- Cadastrar o livro ---")
    title = input("Digite o Titulo do livro: ")
    print("--- Cadastrar o Autor ---")
    name = input("Digite o nome do autor: ")
    dataBirth = tryDate("Digite a data de nascimento do Autor DD/MM/AAAA: ")
    author = createAuthor(name, dataBirth)
    authors.append(author)           
    book = createBook(title, author)
    books.append(book)
    print("--- Livro cadastrado com sucesso! ---")

def buscarLivro():
    title_or_id = input("Digite o titulo do Livro ou ID: ")
    getBook(title_or_id)

def editarLivro():
    title_or_id = input("Digite o titulo do Livro ou ID: ")
    editBooks(title_or_id)

def excluirLivro():
    title_or_id = input("Digite o titulo do livro ou ID: ")
    deleteBooks(title_or_id)

def cadastrarAluno():
    print("--- Cadastrar Aluno ---")
    name = input("Digite o nome do Aluno: ")
    dataBirth = tryDate("Digite a data de nascimento do Aluno DD/MM/AAAA: ")
    email = input("Digite o email do Aluno: ")
    student = createStudent(name,dataBirth,email)
    students.append(student)
    print("--- Aluno Cadastrado com sucesso ---")

def realizarEmprestimo():
    title_or_id = input("Digite o ID ou Título do livro para empréstimo: ")
    if bookAvilable(title_or_id):
        student_identifier = input("Digite o ID do Aluno ou nome do Aluno: ")
        if loanBook(title_or_id, student_identifier):
            print("--- Empréstimo registrado com sucesso ---")
        else:
            print("--- Falha ao registrar o empréstimo ---")
    else:
        print("--- Não é possivel realizar o empréstimo ---")

def finalizarEmpréstimo():
    title_or_id = input("Digite o ID do livro ou Título do livro para finalizar o empréstimo: ")
    returnBook(title_or_id)

def historicoEmprestimoAluno():
    listStudent()
    student_identifier = input("Digite o ID ou nome do Aluno para ver o histórico: ")
    listStudentHistory(student_identifier)

def historicoEmprestimoLivro():
    listBooks()
    book_identifier = input("Digite o ID do livro: ")
    bookLoanHistory(book_identifier)

def buscarLivroAutor():
    authorBook = input("Bucar pelo nome do Autor: ")
    authorTheBook(authorBook)

def excluirAluno():
    name_or_id = input("Digite o nome do Aluno ou ID: ")
    deleteStudents(name_or_id)

def editarAluno():
    name_or_id = input("Digite o nome do Aluno ou ID: ")
    editStudents(name_or_id)

def editarAutor():
    name_or_id = input("Digite o ID ou nome do autor: ")
    editAuthor(name_or_id)

def excluirAutor():
    name_or_id = input("Digite o ID ou nome do Autor:")
    deleteAutor(name_or_id)

def Menu():
    while True:
        print("\n--- Bem-vindo ao sistema da Biblioteca ---\n")
        print("1 .Cadastrar Livro")
        print("2 .Buscar Livro")
        print("3 .Editar Livro")
        print("4 .Excluir Livro")
        print("5 .Lista de Livros")
        print("6 .Cadastrar Aluno")
        print("7 .Lista de Alunos")
        print("8 .Editar Aluno")
        print("9 .Excluir Aluno")
        print("10 .Editar Autor")
        print("11. Excluir Autor")
        print("12 .Lista de Autor")
        print("13 .Buscar Livro pelo Autor")
        print("14 .Realizar empréstimo")
        print("15 .Finalizar empréstimo")
        print("16 .Histórico de Empréstimo do Aluno")
        print("17 .Histórico de Empréstimo do Livro")
        print("18 .Sair \n")
        opcao = tryInput("Escolha uma opção: ")

        if opcao == 1:
            cadastrarLivro()

        elif opcao == 2:
            buscarLivro()
           
        elif opcao == 3:
            editarLivro()

        elif opcao == 4:
            excluirLivro()
            
        elif opcao == 5:
            listBooks()

        elif opcao == 6:
            cadastrarAluno()

        elif opcao == 7:
            listStudent()

        elif opcao == 8:
            editarAluno()

        elif opcao == 9:
            excluirAluno()

        elif opcao == 10:
            editarAutor()

        elif opcao == 11:
            excluirAutor()

        elif opcao == 12:
            listAuthor()

        elif opcao == 13:
            buscarLivroAutor()

        elif opcao == 14:
            realizarEmprestimo()

        elif opcao == 15:
            finalizarEmpréstimo()
        
        elif opcao == 16:
            historicoEmprestimoAluno()

        elif opcao == 17:
            historicoEmprestimoLivro()

        elif opcao == 18:
            print("--- Sistema Finalizado ---")
            break

        else:
            print("Opção Inválida, digite novamente.")
Menu()
