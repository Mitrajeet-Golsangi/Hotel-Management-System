function getCookie(cname) {
	let name = cname + "=";
	let decodedCookie = decodeURIComponent(document.cookie);
	let ca = decodedCookie.split(";");
	for (let i = 0; i < ca.length; i++) {
		let c = ca[i];
		while (c.charAt(0) == " ") {
			c = c.substring(1);
		}
		if (c.indexOf(name) == 0) {
			return c.substring(name.length, c.length);
		}
	}
	return "";
}

function submitForm(url) {
	const data = JSON.stringify({
		quantity: document.getElementById("quantity").value,
		smoking: document.getElementById("smoking").checked,
	});

	const csrftoken = getCookie("csrftoken");

	fetch(url, {
		method: "POST",
		headers: {
			Accept: "application/json, text/plain, */*",
			"Content-Type": "application/json",
			"X-CSRFToken": csrftoken,
		},
		body: data,
	})
		.then((res) => res.json())
		.then((data) => {
			const d = JSON.parse(data.data);
			let i = 0;
			const tbody = document.getElementById("available_rooms_tbody");

			tbody.innerHTML = "";

			if (d.length > 0) {
				d.forEach((e) => {
					const row = document.createElement("tr");
					i++;

					row.innerHTML = `<tr>
				    <td class="px-4 py-2 font-medium text-gray-900 whitespace-nowrap">
                    ${i}
				    </td>
				    <td class="px-4 py-2 text-gray-700 whitespace-nowrap">${e.fields.capacity}</td>
				    <td class="px-4 py-2 text-gray-700 whitespace-nowrap">
                    ${e.fields.room_type}
				    </td>
				    <td class="px-4 py-2 text-gray-700 whitespace-nowrap">${e.fields.floor}</td>
				    <td class="px-4 py-2 text-gray-700 whitespace-nowrap">${e.fields.rate}</td>
				    <td class="px-4 py-2 text-gray-700 whitespace-nowrap"><a href="/book/${e.pk}/" class="rounded-full bg-teal-600 text-white text-sm font-medium hover:bg-teal-700 p-2">Book Now!</a></td>
                    </tr>`;

					tbody.appendChild(row);
				});
			} else {
				const row = document.createElement("tr");
				row.innerHTML = `<td colspan="6" ><p class="max-w-md mx-auto mt-4 text-center text-gray-500">
                    OOPS!🤭 Looks Like we cannot meet your requirements just now. Maybe try again later, you never know ..
                    </p></td>`;
				tbody.appendChild(row);
			}
		});

	// displayData(url);
}
