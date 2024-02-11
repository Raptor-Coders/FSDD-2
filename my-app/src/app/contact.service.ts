import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Icontact } from './icontact';
import { IcourseInterface } from './icourse.interface';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ContactService {
  private serviceBaseUrl = 'http://localhost:8000/';
  constructor(private http: HttpClient) {}

  createContact(contactData: Icontact): Observable<any> {
    console.log('Contact data', contactData);
    return this.http.post<IcourseInterface[]>(
      `${this.serviceBaseUrl}/api/contacts/`,
      {
        fullname: contactData.name,
        email: contactData.email,
        phone: contactData.subject,
        query: contactData.message,
      }
    );
  }
}
